&_POST;

($sec,$min,$hour,$day,$mon,$year) = localtime(time);
$config{'CSVDownloadName'} = sprintf("%04d-%02d-%02d.csv",$year+1900,$mon+1,$day,$hour,$min,$sec);

if($config{"password"} ne $null && $config{"password"} eq $_POST{'password'} && ($config{'CSVDownloadURIPassCode'} eq $null || $config{'CSVDownloadURIPassCode'} eq $_GET{'key'})){
	my $HostName = &_GETHOST;
	if(($config{'CSVDownloadHostName'} eq $HostName || $config{'CSVDownloadHostName'} eq $null) && (grep(/^$ENV{'REMOTE_ADDR'}$/,(split(/\,/,$config{'CSVDownloadIPAddress'}))) > 0 || $config{'CSVDownloadIPAddress'} eq $null)){
		if($_POST{'method'} eq 'download'){
			if(-f $config{"file.csv"}){
				$csv = &_LOAD($config{"file.csv"});
				if($config{'CryptKey'} ne $null){
					$csv = &_CSVDECRYPT($csv);
				}
				$csv =~ s/\n\n/\n/ig;
				use Encode;
				Encode::from_to($csv,'utf8','cp932');
				#$size = -s $config{"file.csv"};
				print "Content-type: application/octet-stream;charset=Shift_JIS; name=\"$config{'CSVDownloadName'}\"\n";
				print "Content-Disposition: attachment; filename=\"$config{'CSVDownloadName'}\"\n";
				print "Accept-Ranges: bytes\n\n";
				#print "Content-length: ${size}\n\n";
				print $csv;
			}
			else {
				&_Error(0);
			}
		}
		elsif($_POST{'method'} eq 'delete'){
			my $format = "";
			if(-f $config{'CSVexport'}){
				$format = &_LOAD($config{'CSVexport'});
				$format =~ s/<_//ig;
				$format =~ s/_>//ig;
			}
			&_SAVE($config{"file.csv"},$format);
			print "Location: $ENV{'HTTP_REFERER'}#Complete\n\n";
		}
	}
	else {
		&_Error(0);
	}
}
else {
	if($config{"password"} ne $null){
		if($config{'CSVDownloadURIPassCode'} eq $null || $config{'CSVDownloadURIPassCode'} eq $_GET{'key'}){
			## Display Process
			$html = &_LOAD("./librarys/CSVExport/download.tpl");
			$HostName = &_GETHOST;
			$html =~ s/_%%HostName%%_/$HostName/ig;
			$html =~ s/_%%IPAddres%%_/$ENV{'REMOTE_ADDR'}/ig;
			print "Pragma: no-cache\n";
			print "Cache-Control: no-cache\n";
			print "Content-type: text/html; charset=UTF-8\n\n";
			print $html;
		}
		else {
			&_Error(0);
		}
	}
	else {
		&_Error(0);
	}
}
exit;