import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import { useContext, useRef, useState } from 'react';
import {
  CheckBoxDefault,
  ComboBox,
  ComboBoxDefault,
  ConfigSymbol,
  configSymbolApi,
  PluginConfigContext,
  symbolUtilApi,
  useComboSymbol,
  useIntegerSymbol,
  useStringSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import { Dropdown } from 'primereact/dropdown';
import { GetButton } from 'clock-common/lib/Components/NodeType';
import FrequencyLabelComponent from 'clock-common/lib/Components/LabelComponent/FrequencyLabelComponent';
import { Dialog } from 'primereact/dialog';
import USBPLLAutoCalculation from './USBPLLAutoCalculation';
import { getSymbolValue } from 'clock-common/lib/Tools/Tools';
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
let usbOld = -1;
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
  const UPLLCON_UPLL_BYP_VALUE = useComboSymbol({
    componentId,
    symbolId: 'UPLLCON_UPLL_BYP_VALUE'
  });
  const usbClockFreq = useStringSymbol({ componentId, symbolId: 'USBCLK' });
  const poscFreqHook = useIntegerSymbol({
    componentId,
    symbolId: 'POSC_OUT_FREQ'
  });

  const [dialogStatus, setdialogStatus] = useState(false);

  function usbAutoCalculationButtonClicked() {
    getSymbolValue(componentId, 'USBCLK').then((value) => {
      usbOld = value;
    });
    setdialogStatus(true);
  }

  const dialogClosed = (acceptStatus: boolean) => {
    if (!acceptStatus) {
      if (usbOld !== Number(usbClockFreq.value)) {
        configSymbolApi.setValue(componentId, 'UPLL_REQUESTED_FOUT', Number(usbOld));
      }
    }
    symbolUtilApi.clearUserValue(componentId, ['UPLL_ERROR_PERC']);
    setdialogStatus(false);
  };

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
      <ComboBox
        comboSymbolHook={UPLLCON_UPLL_BYP_VALUE}
        hidden={false}
        disabled={UPLLCON_UPLL_BYP_VALUE.readOnly || !UPLLCON_UPLL_BYP_VALUE.visible}
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

      <GetButton
        buttonDisplayText={'Auto Calculate'}
        className={props.cx('USBAutoCalculate')}
        toolTip={'click here for USB Auto Clalucation'}
        buttonClick={usbAutoCalculationButtonClicked}
      />

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
      <Dialog
        header='Auto Calculate USB PLL Dividers'
        visible={dialogStatus}
        maximizable={true}
        style={{ width: '45rem', height: '22rem' }}
        onHide={() => {
          dialogClosed(false);
        }}>
        <USBPLLAutoCalculation
          componentId={componentId}
          usbPLLClk={Number(usbClockFreq.value)}
          usbclkPllInputFreq={poscFreqHook.value}
          close={(acceptStatus) => {
            dialogClosed(acceptStatus);
          }}
        />
      </Dialog>
    </div>
  );
};

export default USBPLLController;
