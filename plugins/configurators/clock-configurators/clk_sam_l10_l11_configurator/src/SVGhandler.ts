import $ from 'jquery';

export async function initializeSVG(componentId: string, cx: (...classNames: string[]) => string) {
  $('#clk_sam_l10_l11-main-image').addClass(cx('main-block-diagram'));
}

export async function updateSVG(shared:boolean) {
  const sharedPin =$('#clk_sam_l10_l11-gclk-input-pin')
  if(shared){
    sharedPin.css('opacity', '-1');
  }
  else{
    sharedPin.css('opacity', '1');
  }
    
}
