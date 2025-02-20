import { component_id } from './MainBlock';
import { AddPlainLabel, AddInputFormatSymbolLabel } from '../clock-common/utils/ClockLabelUtils';
import CPUCLKCSSController from './BoldLabelController/CPUCLKCSSController';
import CLKUSBUSBSController from './BoldLabelController/CLKUSBUSBSController';
import StateLabel from '@mplab_harmony/harmony-plugin-ui/build/components/StateLabel';
import { GetSymbolValue } from '@mplab_harmony/harmony-plugin-core-service';
import { GetStyle } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import { ChangeCustomLabelComponentState } from '@mplab_harmony/harmony-plugin-ui/build/utils/ComponentStateChangeUtils';

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
        {/* {AddInputFormatSymbolLabel('label_pclkMdiv', component_id, 'CLK_CPU_CKR_MDIV', GetMDIVText)} */}
        <StateLabel
          labelId={'label_pclkMdiv'}
          labelDisplayText={GetMDIVText(GetSymbolValue(component_id, 'CLK_CPU_CKR_MDIV'))}
          labelStyle={GetStyle('label_pclkMdiv')}
          className={'label_pclkMdiv'}
        />
        {AddInputFormatSymbolLabel_Custom(
          'label_pclk_1',
          component_id,
          'CLK_CPU_CKR_MDIV',
          AddMDivType
        )}

        {AddInputFormatSymbolLabel('label_usbdivVal', component_id, 'CLK_USB_USBDIV', AddDivioType)}

        {AddInputFormatSymbolLabel(
          'label_pllaDivpmcVal',
          component_id,
          'CLK_PLLA_DIVPMC',
          AddDivioTypePLLA
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

function AddInputFormatSymbolLabel_Custom(
  id: string,
  component_id: string,
  symbolId: string,
  InputFormat: (arg0: any) => void,
  className?: any
) {
  function customLabelConfigOnSymbolChange(symbolId: any, value: any) {
    ChangeCustomLabelComponentState(symbolId, InputFormat(value), null, null, null);

    const label = document.getElementById('label_pclkMdiv');
    if (label) {
      label.textContent = GetMDIVText(value) ?? '';
    }
  }
  try {
    return (
      <div>
        <StateLabel
          labelId={id}
          labelDisplayText={InputFormat(GetSymbolValue(component_id, symbolId))}
          labelStyle={GetStyle(id)}
          symbolListeners={[symbolId]}
          className={className}
          customLabelConfigOnSymbolChange={customLabelConfigOnSymbolChange}
        />
      </div>
    );
  } catch (err) {
    /* empty */
  }
}

function GetMDIVText(text: any) {
  try {
    let divValue = text.replace('PCK_DIV', '');
    divValue = divValue.replace('DIV', '');
    divValue = divValue.replace('CLK', '');
    divValue = divValue === 'EQ_PCK' ? '1' : divValue;
    return '/ ' + divValue;
  } catch (err) {}
}

export function AddDivioType(text: string) {
  try {
    const newvalue = '( ' + text + ' + 1 )';
    return '/ ' + newvalue;
  } catch (err) {}
}

export function AddDivioTypePLLA(text: string) {
  try {
    const newvalue = '(2*( ' + text + ' + 1 ))';
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
