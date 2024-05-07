import { stringSymbolApi } from '@mplab_harmony/harmony-plugin-client-lib';
import $ from 'jquery';

export async function initializeSVG(componentId: string, cx: (...classNames: string[]) => string) {
  const productFamily = await stringSymbolApi.getValue('core', 'PRODUCT_FAMILY');
  if(productFamily==='PIC32CX_MT'){
    const sama7g5Pinlabels = $('#adc_44134-input-pins-sama7g5')
    const lastPin = $('#adc_44134-last-input-pin > text')
    const pinLine = $('#adc_44134-input-pins-for-sam72')
    sama7g5Pinlabels.css('opacity', '-1');
    lastPin.text('ADC_AD(n-1)');
    pinLine.css('opacity', '-1');
  }
  else{
    const pinLine =$('#adc_44134-input-pins-pic32cx-mt')
   
    pinLine.css('opacity', '-1');
  }
  $('#adc_44134-main-image').addClass(cx('mainBlockDiagram'));
}
