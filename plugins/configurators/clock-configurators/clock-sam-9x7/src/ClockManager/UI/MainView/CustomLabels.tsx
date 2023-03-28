import { component_id } from './MainBlock';
import { AddPlainLabel, AddInputFormatSymbolLabel } from 'clock-common/lib/utils/ClockLabelUtils';
import CPUCLKCSSController from './BoldLabelController/CPUCLKCSSController';
import CLKUSBUSBSController from './BoldLabelController/CLKUSBUSBSController';

export function AddCustomLabels() {
  try {
    return (
      <div>
        {AddPlainLabel('label_enableGenerator', 'Enable Generator Initialization')}

        {AddInputFormatSymbolLabel(
          'label_pclkPres',
          component_id,
          'CLK_CPU_CKR_PRES',
          GetDiVAddedText
        )}
        {AddInputFormatSymbolLabel(
          'label_pclkMdiv',
          component_id,
          'CLK_CPU_CKR_MDIV',
          GetDiVAddedText
        )}
        {AddInputFormatSymbolLabel('label_pclk_1', component_id, 'CLK_CPU_CKR_MDIV', AddMDivType)}

        {AddInputFormatSymbolLabel('label_usbdivVal', component_id, 'CLK_USB_USBDIV', AddDivioType)}

        {AddInputFormatSymbolLabel(
          'label_pllaDivpmcVal',
          component_id,
          'CLK_PLLA_DIVPMC',
          AddDivioType
        )}

        {AddInputFormatSymbolLabel(
          'label_audioPllDivpmcVal',
          component_id,
          'CLK_AUDIOPLL_DIVPMC',
          AddDivioType
        )}
        {AddInputFormatSymbolLabel(
          'label_audiopllDivioVal',
          component_id,
          'CLK_AUDIO_IOPLLCK_DIVIO',
          AddDivioType
        )}

        {AddInputFormatSymbolLabel(
          'label_lvdspllDIVPMCVal',
          component_id,
          'CLK_LVDSPLL_DIVPMC',
          AddDivioType
        )}

        <CPUCLKCSSController symboListenerValue={'CLK_CPU_CKR_CSS'} />
        <CLKUSBUSBSController symboListenerValue={'CLK_USB_USBS'} />
      </div>
    );
  } catch (err) {}
}

function GetDiVAddedText(text: any) {
  try {
    let divValue = RemoveDiv(text);
    divValue = divValue.replace('CLK', '');
    divValue = divValue.replace('DIV', '');
    return '/ ' + divValue;
  } catch (err) {}
}

export function AddDivioType(text: string) {
  try {
    const newvalue = '( ' + text + ' + 1 )';
    return '/ ' + newvalue;
  } catch (err) {}
}

function AddMDivType(text: string) {
  try {
    const newValue = text.replace(/^\D+/g, '');
    let val = 1;
    if (newValue.length > 0) {
      if (+newValue > 1) {
        val = +newValue / 2;
      }
    }
    return '/ ' + val;
  } catch (err) {}
}

function RemoveDiv(value: string) {
  const newValue = value.split('_');
  return newValue[1];
}
