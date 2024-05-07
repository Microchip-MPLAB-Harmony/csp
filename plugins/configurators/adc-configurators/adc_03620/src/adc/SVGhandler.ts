import $ from 'jquery';

export async function initializeSVG(componentId: string, cx: (...classNames: string[]) => string) {
  $('#adc_03260-main-image').addClass(cx('mainBlockDiagram'));
}

export async function updateSVG(shared:boolean) {
  const sharedPin =$('#adchs_02508-shared-input-pins')
  const dedicatedPin =$('#adchs_02508-dedicated-input-pins')
  if(shared){
    dedicatedPin.css('opacity', '-1');
    sharedPin.css('opacity', '1');
  }
  else{
    sharedPin.css('opacity', '-1');
    dedicatedPin.css('opacity', '1');
   
  }
    
}
