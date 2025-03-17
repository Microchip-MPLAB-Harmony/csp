import $ from 'jquery';

export async function initializeSVG(componentId: string, cx: (...classNames: string[]) => string) {
  $('#clk_sam_l21-main-image').addClass(cx('main-block-diagram'));
}

export async function updateSVG(shared:boolean) {
  const sharedPin =$('#clk_sam_l21-gclk-input-pin')
  if(shared){
    sharedPin.css('opacity', '-1');
  }
  else{
    sharedPin.css('opacity', '1');
  }
    
}
