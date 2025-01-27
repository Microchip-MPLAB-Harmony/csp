import $ from 'jquery';
 
export async function initializeSVG(componentId: string, cx: (...classNames: string[]) => string) {
  $('#clk-dspic33-main-image').addClass(cx('main-image'));
}

export async function updateSVGForClockGen1Block(showClockDivider:boolean) {
  const clkDividerBlk =$('#data-clk-divider-block')
  if(showClockDivider){
    clkDividerBlk.css('opacity', '-1');
  }
  else{
    clkDividerBlk.css('opacity', '1');
  }
}

export async function updateSVGForCommonClockBlock(showClockDivider:boolean) {
  const clkDividerBlk =$('#data-common-clk-divider-block')
  if(showClockDivider){
    clkDividerBlk.css('opacity', '-1');
  }
  else{
    clkDividerBlk.css('opacity', '1');
  }
}