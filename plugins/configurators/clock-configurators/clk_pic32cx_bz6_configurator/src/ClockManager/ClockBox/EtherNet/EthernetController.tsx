import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import { useContext, useEffect, useState } from 'react';
import {
  CheckBoxDefault,
  ComboBoxDefault,
  configSymbolApi,
  PluginConfigContext,
  useComboSymbol,
  useIntegerSymbol,
  useStringSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import { Dropdown } from 'primereact/dropdown';
import { GetButton } from 'clock-common/lib/Components/NodeType';
import { Dialog } from 'primereact/dialog';
import EthernetAutoCalculation from './EthernetAutoCalculation';
import FrequencyLabelComponent from 'clock-common/lib/Components/LabelComponent/FrequencyLabelComponent';
import { GetClockDisplayFreqValue } from 'clock-common/lib/Tools/Tools';
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

  const [dialogStatus, setdialogStatus] = useState(false);
  const [ethclokoutEnFreq, setethclockoutEnFreq] = useState(
    GetClockDisplayFreqValue(Number(eth1ClockFreq.value))
  );

  function ethernetAutoCalculationButtonClicked() {
    setdialogStatus(true);
  }

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

      <ComboBoxDefault
        componentId={componentId}
        symbolId='EPLLCON_ECLKOUTEN_VALUE'
        className={props.cx('ethclkouten')}
      />
      <ComboBoxDefault
        componentId={componentId}
        symbolId='EPLLCON_EPLL_BYP_VALUE'
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

      {/* <GetButton
        buttonDisplayText={'Auto Calculate'}
        className={props.cx('EWautoCalculate')}
        toolTip={'click here for Ethernet Auto Clalucation'}
        buttonClick={ethernetAutoCalculationButtonClicked}
      /> */}

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
        onHide={() => {
          setdialogStatus(false);
        }}>
        <EthernetAutoCalculation />
      </Dialog>
    </div>
  );
};

export default EthernetController;
