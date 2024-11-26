import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import { useContext, useEffect, useState } from 'react';
import {
  CheckBoxDefault,
  ComboBox,
  ComboBoxDefault,
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
import { Dialog } from 'primereact/dialog';
import FrequencyLabelComponent from 'clock-common/lib/Components/LabelComponent/FrequencyLabelComponent';
import { GetClockDisplayFreqValue, getSymbolValue } from 'clock-common/lib/Tools/Tools';
import EthernetAutoCalculation from './EthernetAutoCalculation';
const settingsArray = [
  'EPLL_ENABLE',
  'EPLLCON_EPLLPOSTDIV1_VALUE',
  'EPLLCON_EPLLFBDIV_VALUE',
  'EPLLCON_EPLLREFDIV_VALUE',
  'EPLLPOSTDIV2',
  'EPLLCON_ECLKOUTEN_VALUE',
  'EPLLCON_EPLL_BYP_VALUE',
  'EPLLCON_EPLLBSWSEL_VALUE',
  'EPLLCON_EPLLPWDN_VALUE',
  'EPLLCON_EPLLFLOCK_VALUE',
  'EPLLCON_EPLLRST_VALUE'
];
const epllDiv1Options = getDivOptions(1, 63);
const epllfbDivOptions = getDivOptions(16, 1023);
const epllRefDivOptions = getDivOptions(1, 63);
function getDivOptions(startValue: number, endValue: number) {
  let options = [];
  for (let i = startValue; i <= endValue; i++) {
    options[i] = 'DIV_' + i;
  }
  return options;
}
let ethclk1Old = -1;
let ethclk2Old = -1;

const EthernetController = (props: {
  controllerData: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const ethClkOutEn = useComboSymbol({
    componentId,
    symbolId: 'EPLLCON_ECLKOUTEN_VALUE'
  });
  const eth1ClockFreq = useStringSymbol({
    componentId,
    symbolId: 'ETHCLK1'
  });
  const eth2ClockFreq = useStringSymbol({
    componentId,
    symbolId: 'ETHCLK2'
  });
  useEffect(() => {
    if (ethClkOutEn.value === 'Enable') {
      setethclockoutEnFreq(GetClockDisplayFreqValue(Number(eth1ClockFreq.value)));
    } else {
      setethclockoutEnFreq('0 Hz');
    }
  }, [eth1ClockFreq.value, ethClkOutEn.value]);

  const epllDiv1 = useIntegerSymbol({
    componentId,
    symbolId: 'EPLLCON_EPLLPOSTDIV1_VALUE'
  });
  const epllDiv2 = useIntegerSymbol({
    componentId,
    symbolId: 'EPLLPOSTDIV2'
  });

  const epllfbdivValue = useIntegerSymbol({
    componentId,
    symbolId: 'EPLLCON_EPLLFBDIV_VALUE'
  });
  const epllRefDivValue = useIntegerSymbol({
    componentId,
    symbolId: 'EPLLCON_EPLLREFDIV_VALUE'
  });

  const primaryOScilaltor = useComboSymbol({
    componentId,
    symbolId: 'CONFIG_POSCMOD'
  });
  const poscFreqHook = useIntegerSymbol({
    componentId,
    symbolId: 'POSC_OUT_FREQ'
  });

  const EPLLCON_EPLL_BYP_VALUE = useComboSymbol({
    componentId,
    symbolId: 'EPLLCON_EPLL_BYP_VALUE'
  });
  const EPLLCON_ECLKOUTEN_VALUE = useComboSymbol({
    componentId,
    symbolId: 'EPLLCON_ECLKOUTEN_VALUE'
  });

  const [dialogStatus, setdialogStatus] = useState(false);
  const [ethclokoutEnFreq, setethclockoutEnFreq] = useState(
    GetClockDisplayFreqValue(Number(eth1ClockFreq.value))
  );

  function ethernetAutoCalculationButtonClicked() {
    getSymbolValue(componentId, 'ETHCLK1').then((value) => {
      ethclk1Old = value;
    });
    getSymbolValue(componentId, 'ETHCLK2').then((value) => {
      ethclk2Old = value;
    });
    setdialogStatus(true);
  }

  const dialogClosed = (acceptStatus: boolean) => {
    if (!acceptStatus) {
      if (ethclk1Old !== Number(eth1ClockFreq.value)) {
        configSymbolApi.setValue(componentId, 'EPLL1_REQUESTED_FOUT', Number(ethclk1Old));
      }
      if (ethclk2Old !== Number(eth2ClockFreq.value)) {
        configSymbolApi.setValue(componentId, 'EPLL2_REQUESTED_FOUT', Number(ethclk2Old));
      }
    }
    symbolUtilApi.clearUserValue(componentId, ['EPLL1_ERROR_PERC']);
    symbolUtilApi.clearUserValue(componentId, ['EPLL2_ERROR_PERC']);
    setdialogStatus(false);
  };

  return (
    <div>
      <Dropdown
        value={'DIV_' + epllRefDivValue.value}
        options={epllRefDivOptions}
        onChange={(e) => {
          configSymbolApi.setValue(
            componentId,
            'EPLLCON_EPLLREFDIV_VALUE',
            parseInt(e.value.replace('DIV_', ''))
          );
        }}
        className={props.cx('ewpllidiv')}
      />
      <PlainLabel
        disPlayText={'' + epllRefDivValue.value}
        booldStatus={true}
        className={props.cx('lbl_ewpllinputdiv')}
      />

      <Dropdown
        value={'DIV_' + epllfbdivValue.value}
        options={epllfbDivOptions}
        onChange={(e) => {
          configSymbolApi.setValue(
            componentId,
            'EPLLCON_EPLLFBDIV_VALUE',
            parseInt(e.value.replace('DIV_', ''))
          );
        }}
        className={props.cx('ewpllfbdiv')}
      />
      <PlainLabel
        disPlayText={'' + epllfbdivValue.value}
        booldStatus={true}
        className={props.cx('lbl_ewpllfbdiv')}
      />
      <Dropdown
        value={'DIV_' + epllDiv1.value}
        options={epllDiv1Options}
        onChange={(e) => {
          configSymbolApi.setValue(
            componentId,
            'EPLLCON_EPLLPOSTDIV1_VALUE',
            parseInt(e.value.replace('DIV_', ''))
          );
        }}
        className={props.cx('ewpllodiv1')}
      />
      <PlainLabel
        disPlayText={'' + epllDiv1.value}
        booldStatus={true}
        className={props.cx('lbl_ewplloutputdiv1')}
      />

      <Dropdown
        value={'DIV_' + epllDiv2.value}
        options={epllDiv1Options}
        onChange={(e) => {
          configSymbolApi.setValue(
            componentId,
            'EPLLPOSTDIV2',
            parseInt(e.value.replace('DIV_', ''))
          );
        }}
        className={props.cx('ewpllodiv2')}
      />
      <PlainLabel
        disPlayText={'' + epllDiv2.value}
        booldStatus={true}
        className={props.cx('lbl_ewplloutputdiv2')}
      />

      <ComboBox
        comboSymbolHook={EPLLCON_ECLKOUTEN_VALUE}
        hidden={false}
        disabled={EPLLCON_ECLKOUTEN_VALUE.readOnly || !EPLLCON_ECLKOUTEN_VALUE.visible}
        className={props.cx('ethclkouten')}
      />
      <ComboBox
        comboSymbolHook={EPLLCON_EPLL_BYP_VALUE}
        hidden={false}
        disabled={EPLLCON_EPLL_BYP_VALUE.readOnly || !EPLLCON_EPLL_BYP_VALUE.visible}
        className={props.cx('ewbypass')}
      />
      <ComboBoxDefault
        componentId={componentId}
        symbolId='EPLLCON_EPLLBSWSEL_VALUE'
        className={props.cx('ewpll_bwsel1')}
      />

      <CheckBoxDefault
        componentId={componentId}
        symbolId='EPLL_ENABLE'
        className={props.cx('ewpllEnable')}
      />

      <FrequencyLabelComponent
        componentId={componentId}
        symbolId={'ETHCLK1'}
        className={props.cx('lbl_cm_epllFreq1')}
      />
      <FrequencyLabelComponent
        componentId={componentId}
        symbolId={'ETHCLK2'}
        className={props.cx('lbl_cm_epllFreq2')}
      />
      <PlainLabel
        disPlayText='PFD'
        booldStatus={true}
        className={props.cx('lbl_ewpllpfd')}
      />

      {primaryOScilaltor.value !== 'HS' && (
        <PlainLabel
          disPlayText='POSC is OFF'
          booldStatus={true}
          redColorStatus={true}
          className={props.cx('lbl_err_posc_ew')}
        />
      )}

      <PlainLabel
        disPlayText={ethclokoutEnFreq}
        className={props.cx('ethclkOutENFreq')}
      />

      <GetButton
        buttonDisplayText={'Auto Calculate'}
        className={props.cx('EWautoCalculate')}
        toolTip={'click here for Ethernet Auto Clalucation'}
        buttonClick={ethernetAutoCalculationButtonClicked}
      />

      <SettingsDialog
        tooltip='Clock Settings Configuration'
        componentId={componentId}
        className={props.cx('ewPll_settings')}
        symbolArray={settingsArray}
        dialogWidth='50rem'
        dialogHeight='47rem'
      />
      <ResetSymbolsIcon
        tooltip='Reset Clock symbols to default value'
        className={props.cx('ewPLL_reset')}
        componentId={componentId}
        resetSymbolsArray={settingsArray}
      />
      <Dialog
        header='Auto Calculate EW PLL Dividers'
        visible={dialogStatus}
        maximizable={true}
        style={{ width: '45rem', height: '34rem' }}
        onHide={() => {
          dialogClosed(false);
        }}>
        <EthernetAutoCalculation
          componentId={componentId}
          ethclk1={Number(eth1ClockFreq.value)}
          ethclk2={Number(eth2ClockFreq.value)}
          ethclkPllInputFreq={poscFreqHook.value}
          close={(acceptStatus) => {
            dialogClosed(acceptStatus);
          }}
        />
      </Dialog>
    </div>
  );
};

export default EthernetController;
