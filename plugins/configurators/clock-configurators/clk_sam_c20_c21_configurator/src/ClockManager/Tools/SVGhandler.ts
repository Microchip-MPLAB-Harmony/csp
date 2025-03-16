import $ from 'jquery';

export async function initializeSVG(cx: (...classNames: string[]) => string) {
  $('#clk_sam_c20_c21-main-image').addClass(cx('main-block-diagram'));
}

export async function updateSVG(shared: boolean) {
  const sharedPin = $('#clk_sam_c20_c21-gclk8Line');
  if (shared) {
    sharedPin.css('opacity', '-1');
  } else {
    sharedPin.css('opacity', '1');
  }
}
