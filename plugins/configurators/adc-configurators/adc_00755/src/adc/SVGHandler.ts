import $ from 'jquery';
import { getMaxChannel } from './ADCUtil';

export async function initializeSVG(componentId: string, cx: (...classNames: string[]) => string) {
  const maxChannel = await getMaxChannel(componentId, 'AD1CON2__CSCNA');

  $('#adc_00755-ANz > text').text(`AN${maxChannel}`);
  $('#adc_00755-main-image').addClass(cx('main-block-diagram'));
}

export async function updateNegativeInputLabels(
  negativeInputAValue: string,
  negativeInputBValue: string,
  isNegativeInputBEnabled: boolean
) {
  const AN1Pin = $('#adc_00755-negativePin2 > text');
  const VREFLPin = $('#adc_00755-negativePin1 > text');

  if (negativeInputAValue.toUpperCase() === 'AN1') {
    AN1Pin.css('font-weight', 'bold');
  } else if (isNegativeInputBEnabled && negativeInputBValue.toUpperCase() === 'AN1') {
    AN1Pin.css('font-weight', 'bold');
  } else {
    AN1Pin.css('font-weight', 'normal');
  }

  if (negativeInputAValue.toUpperCase() === 'VREFL') {
    VREFLPin.css('font-weight', 'bold');
  } else if (isNegativeInputBEnabled && negativeInputBValue.toUpperCase() === 'VREFL') {
    VREFLPin.css('font-weight', 'bold');
  } else {
    VREFLPin.css('font-weight', 'normal');
  }
}
