import { stringSymbolApi } from '@mplab_harmony/harmony-plugin-client-lib';
import $ from 'jquery';

export async function initializeSVG(componentId: string, cx: (...classNames: string[]) => string) {
  const productFamily = await stringSymbolApi.getValue('core', 'PRODUCT_FAMILY');
  if(productFamily==='SAMRH'){
    const lastPin = $('#adc_44073-last-input-pin > text')
    lastPin.text('ADC_AD15');
    const resultSign =$('#adc_44073-result-sign')
    resultSign.css('opacity', '-1');
    const triggerSelection =$('#adc_44073-trigger-lines')
    triggerSelection.css('opacity', '-1');
    const tcpwm = $('#adc_44073-TCPWM > text')
    tcpwm.text('TC, PWM');
  }
  $('#adc_44073-main-image').addClass(cx('mainBlockDiagram'));
}
