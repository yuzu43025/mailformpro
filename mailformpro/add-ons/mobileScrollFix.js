// �e�I�u�W�F�N�g��position relative���������Ă���ꍇ�A���܂������Ȃ���
mfp.extend.event('elementError',
	function(obj){
		if(mfp.Ready){
			var ua = navigator.userAgent;
			if(ua.indexOf('Mobile') > -1){
				mfp.scroll(obj.id);
			};
		};
	}
);