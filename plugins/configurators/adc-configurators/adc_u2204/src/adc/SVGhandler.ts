import { stringSymbolApi } from '@mplab_harmony/harmony-plugin-client-lib';
import $ from 'jquery';

export async function initializeSVG(componentId: string, cx: (...classNames: string[]) => string) {
  
  $('#adc_u2204-main-image').addClass(cx('mainBlockDiagram'));
}
