import { component_id } from './MainBlock';
import { AddPlainLabel, AddPrefixDivSymbolLabel } from 'clock-common/lib/utils/ClockLabelUtils';
import CPUCLKCSSController from './BoldLabelController/CPUCLKCSSController';
import CLKUSBUSBSController from './BoldLabelController/CLKUSBUSBSController';

export function AddCustomLabels() {
  try {
    return (
      <div>
        {AddPlainLabel('label_enableGenerator', 'Enable Generator Initialization')}

        {AddPrefixDivSymbolLabel(
          'label_pclkPres',
          component_id,
          'CLK_CPU_CKR_PRES',
          GetDiVAddedText
        )}
        {AddPrefixDivSymbolLabel(
          'label_pclkMdiv',
          component_id,
          'CLK_CPU_CKR_MDIV',
          GetDiVAddedText
        )}
        {AddPrefixDivSymbolLabel('label_pclk_1', component_id, 'CLK_CPU_CKR_MDIV', AddMDivType)}

        {AddPrefixDivSymbolLabel('label_usbdivVal', component_id, 'CLK_USB_USBDIV', AddDivioType)}

        {AddPrefixDivSymbolLabel(
          'label_pllaDivpmcVal',
          component_id,
          'CLK_PLLA_DIVPMC',
          AddDivioType
        )}

        {AddPrefixDivSymbolLabel(
          'label_audioPllDivpmcVal',
          component_id,
          'CLK_AUDIOPLL_DIVPMC',
          AddDivioType
        )}
        {AddPrefixDivSymbolLabel(
          'label_audiopllDivioVal',
          component_id,
          'CLK_AUDIO_IOPLLCK_DIVIO',
          AddDivioType
        )}

        {AddPrefixDivSymbolLabel(
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
