my %place = ();
$place{'�c��'} = '�����w';
$place{'����'} = '�É��w';
if($place{$_POST{'�����O'}}){
	$_ENV{'chgdata'} = $place{$_POST{'�����O'}};
}
1;