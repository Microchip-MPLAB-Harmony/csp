import { integerSymbolApi, stringSymbolApi } from '@mplab_harmony/harmony-plugin-client-lib';
import $ from 'jquery';

export async function initializeSVG(componentId: string, cx: (...classNames: string[]) => string) {
  const productFamily = await stringSymbolApi.getValue('core', 'PRODUCT_FAMILY');
  const totalPins = await integerSymbolApi.getValue(componentId, 'ADC_NUM_OF_PINS');

  const vddCore = $('#adc_02805-vdd-core');

  const resultRegisterX = $('#adc_02805-result-register-x > text');
  const resultRegisterY = $('#adc_02805-result-register-y > text');
  const resultRegisterZ = $('#adc_02805-result-register-z > text');
  if (productFamily === 'PIC32MM1387') {
    vddCore.css('opacity', '1');

    resultRegisterX.text('ADC1BUF19');
    resultRegisterY.text('ADC1BUF20');
    resultRegisterZ.text('ADC1BUF21');
  } else {
    vddCore.css('opacity', '0');

    resultRegisterX.text('ADC1BUF13');
    resultRegisterY.text('ADC1BUF14');
    resultRegisterZ.text('ADC1BUF15');
  }

  $('#adc_02805-ANz > text').text(`AN${totalPins - 1}`);
  $('#adc_02805-main-image').addClass(cx('main-block-diagram'));
}
