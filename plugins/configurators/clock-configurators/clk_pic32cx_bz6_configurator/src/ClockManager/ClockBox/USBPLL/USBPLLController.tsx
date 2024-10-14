import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import { useContext } from 'react';
import {
  CheckBoxDefault,
  ComboBoxDefault,
  configSymbolApi,
  PluginConfigContext,
  useComboSymbol,
  useIntegerSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import { Dropdown } from 'primereact/dropdown';
import { GetButton } from 'clock-common/lib/Components/NodeType';
import FrequencyLabelComponent from 'clock-common/lib/Components/LabelComponent/FrequencyLabelComponent';
const settingsArray = [
  'USBPLL_ENABLE',
  'UPLLCON_UPLLPOSTDIV1_VALUE',
  'UPLLCON_UPLLFBDIV_VALUE',
  'UPLLCON_UPLLREFDIV_VALUE',
  'UPLLCON_ECLKOUTEN_VALUE',
  'UPLLCON_UPLL_BYP_VALUE',
  'UPLLCON_UPLLBSWSEL_VALUE',
  'UPLLCON_UPLLPWDN_VALUE',
  'UPLLCON_UPLLFLOCK_VALUE',
  'UPLLCON_UPLLRST_VALUE'
];
const UPLLDiv1Options = getDivOptions(1, 63);
const UPLLfbDivOptions = getDivOptions(16, 1023);
const UPLLRefDivOptions = getDivOptions(1, 63);
function getDivOptions(startValue: number, endValue: number) {
  let options = [];
  for (let i = startValue; i <= endValue; i++) {
    options[i] = 'DIV_' + i;
  }
  return options;
}

const USBPLLController = (props: {
  controllerData: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const UPLLDiv1 = useIntegerSymbol({
    componentId,
    symbolId: 'UPLLCON_UPLLPOSTDIV1_VALUE'
  });

  const UPLLfbdivValue = useIntegerSymbol({
    componentId,
    symbolId: 'UPLLCON_UPLLFBDIV_VALUE'
  });
  const UPLLRefDivValue = useIntegerSymbol({
    componentId,
    symbolId: 'UPLLCON_UPLLREFDIV_VALUE'
  });

  const primaryOScilaltor = useComboSymbol({
    componentId,
    symbolId: 'CONFIG_POSCMOD'
  });

  function usbAutoCalculationButtonClicked() {
    // callPopUp(GenericPopUp, peripheralClockConfig_PopupHeadding, '40vw', '95vh');
  }

  return (
    <div>
      <Dropdown
        value={'DIV_' + UPLLRefDivValue.value}
        options={UPLLRefDivOptions}
        onChange={(e) => {
          configSymbolApi.setValue(
            componentId,
            'UPLLCON_UPLLREFDIV_VALUE',
            parseInt(e.value.replace('DIV_', ''))
          );
        }}
        className={props.cx('upllidiv')}
      />
      <PlainLabel
        disPlayText={'' + UPLLRefDivValue.value}
        booldStatus={true}
        className={props.cx('lbl_upllidiv')}
      />

      <Dropdown
        value={'DIV_' + UPLLfbdivValue.value}
        options={UPLLfbDivOptions}
        onChange={(e) => {
          configSymbolApi.setValue(
            componentId,
            'UPLLCON_UPLLFBDIV_VALUE',
            parseInt(e.value.replace('DIV_', ''))
          );
        }}
        className={props.cx('upllfbdiv')}
      />
      <PlainLabel
        disPlayText={'' + UPLLfbdivValue.value}
        booldStatus={true}
        className={props.cx('lbl_upllfbdiv')}
      />
      <Dropdown
        value={'DIV_' + UPLLDiv1.value}
        options={UPLLDiv1Options}
        onChange={(e) => {
          configSymbolApi.setValue(
            componentId,
            'UPLLCON_UPLLPOSTDIV1_VALUE',
            parseInt(e.value.replace('DIV_', ''))
          );
        }}
        className={props.cx('upllodiv')}
      />
      <PlainLabel
        disPlayText={'' + UPLLDiv1.value}
        booldStatus={true}
        className={props.cx('lbl_upllodiv')}
      />
      <ComboBoxDefault
        componentId={componentId}
        symbolId='UPLLCON_UPLL_BYP_VALUE'
        className={props.cx('uposcen')}
      />
      <ComboBoxDefault
        componentId={componentId}
        symbolId='UPLLCON_UPLLBSWSEL_VALUE'
        className={props.cx('upll_bwsel')}
      />

      <CheckBoxDefault
        componentId={componentId}
        symbolId='USBPLL_ENABLE'
        className={props.cx('usbpllEnable')}
      />
      <FrequencyLabelComponent
        componentId={componentId}
        symbolId={'USBCLK'}
        className={props.cx('lbl_cm_upllFreq')}
      />

      <PlainLabel
        disPlayText='PFD'
        booldStatus={true}
        className={props.cx('lbl_upllpfd1')}
      />

      {primaryOScilaltor.value !== 'HS' && (
        <PlainLabel
          disPlayText='POSC is OFF'
          booldStatus={true}
          redColorStatus={true}
          className={props.cx('lbl_err_posc_upll')}
        />
      )}

      {/* <GetButton
        buttonDisplayText={'Auto Calculate'}
        className={props.cx('USBAutoCalculate')}
        toolTip={'click here for USB Auto Clalucation'}
        buttonClick={usbAutoCalculationButtonClicked}
      /> */}

      <SettingsDialog
        tooltip='Clock Settings Configuration'
        componentId={componentId}
        className={props.cx('usbPLLSettings')}
        symbolArray={settingsArray}
        dialogWidth='50rem'
        dialogHeight='47rem'
      />
      <ResetSymbolsIcon
        tooltip='Reset Clock symbols to default value'
        className={props.cx('usbPLLReset')}
        componentId={componentId}
        resetSymbolsArray={settingsArray}
      />
    </div>
  );
};

export default USBPLLController;
