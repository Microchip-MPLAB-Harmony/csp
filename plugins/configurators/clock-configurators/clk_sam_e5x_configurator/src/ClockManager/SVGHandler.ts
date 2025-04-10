import $ from 'jquery';

export async function initializeSVG(cx: (...classNames: string[]) => string) {
  $('#clk_sam_e5x-main-image').addClass(cx('main-block-diagram'));
}

export async function updateSVG(shared: boolean) {
  const sharedPin = $('#clk_sam_e5x-gclkXLine9');
  if (shared) {
    sharedPin.css('opacity', '-1');
  } else {
    sharedPin.css('opacity', '1');
  }
}