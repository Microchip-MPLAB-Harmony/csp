import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import { useContext, useEffect, useState } from 'react';
import { GetButton } from 'clock-common/lib/Components/NodeType';
import {
  CheckBoxDefault,
  InputNumberDefault,
  PluginConfigContext,
  useBooleanSymbol,
  useComboSymbol,
  useIntegerSymbol,
  useStringSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import ComboRadio from '../../ClientLib/ComboRadio';
import { GetClockDisplayFreqValue } from 'clock-common/lib/Tools/Tools';
import { Dialog } from 'primereact/dialog';
import ReferenceAutoCalculation from './ReferenceAutoCalculation';

const RefClkControllerBoxTemplate = (props: {
  index: string;
  componentId: string;
  cx: (...classNames: string[]) => string;
  RefClkSettingsSymbolArray: string[];
  RefClkController: ControlInterface[];
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const [dialogStatus, setDialogStatus] = useState(false);
  const isRefEnabled = useBooleanSymbol({
    componentId,
    symbolId: 'CONFIG_SYS_CLK_REFCLK' + props.index + '_ENABLE'
  });

  const roseSource = useComboSymbol({
    componentId,
    symbolId: 'CONFIG_SYS_CLK_REFCLK_SOURCE' + props.index
  });

  const freq = useStringSymbol({
    componentId,
    symbolId: 'CONFIG_SYS_CLK_REFCLK' + props.index + '_FREQ'
  });

  function refClkAutoCalculationButtonClicked() {
    setDialogStatus(true);
  }

  return (
    <div>
      <InputNumberDefault
        componentId={componentId}
        symbolId={'CONFIG_SYS_CLK_CONFIG_REFCLKI_PIN'}
        className={props.cx('refclkix1')}
      />
      <InputNumberDefault
        componentId={componentId}
        symbolId={'CONFIG_SYS_CLK_ROTRIM' + props.index}
        className={props.cx('trimvalue1')}
        hidden={!isRefEnabled.value}
      />
      <InputNumberDefault
        componentId={componentId}
        symbolId={'CONFIG_SYS_CLK_RODIV' + props.index}
        className={props.cx('refoscdiv1')}
        hidden={!isRefEnabled.value}
      />
      <CheckBoxDefault
        componentId={componentId}
        symbolId={isRefEnabled.symbolId}
        className={props.cx('cb_refclk_enable1')}
      />
      <CheckBoxDefault
        componentId={componentId}
        symbolId={'CONFIG_SYS_CLK_REFCLK_SIDL' + props.index}
        className={props.cx('checkbox_idlelmode')}
        hidden={!isRefEnabled.value}
      />
      <CheckBoxDefault
        componentId={componentId}
        symbolId={'CONFIG_SYS_CLK_REFCLK_RSLP' + props.index}
        className={props.cx('checkbox_Sleepmode')}
        hidden={!isRefEnabled.value}
      />
      <CheckBoxDefault
        componentId={componentId}
        symbolId={'CONFIG_SYS_CLK_REFCLK' + props.index + '_OE'}
        className={props.cx('cb_refclkoe1')}
        hidden={!isRefEnabled.value}
      />
      <PlainLabel
        disPlayText={props.index}
        booldStatus={true}
        className={props.cx('refClckNumber')}
      />
      <PlainLabel
        disPlayText={props.index}
        booldStatus={true}
        className={props.cx('refclkRefoNumber')}
      />
      <PlainLabel
        disPlayText={'Run in Sleep Mode'}
        className={props.cx('runInSleepModeLabel')}
      />
      <PlainLabel
        disPlayText={'Run in Idle Mode'}
        className={props.cx('runInIdleModeLabel')}
      />
      <PlainLabel
        disPlayText={' Hz'}
        className={props.cx('refclk0FreqHz')}
      />
      <PlainLabel
        disPlayText={isRefEnabled.value ? GetClockDisplayFreqValue(Number(freq.value)) : '0 Hz'}
        className={props.cx('lbl_refClkOxFreq')}
      />
      <ComboRadio
        comboSymbolHook={roseSource}
        classPrefix='refClk0Radio'
        labelClassPrefix='refClk0RadioName'
        classResolver={props.cx}></ComboRadio>
      <SettingsDialog
        tooltip={'Refclock ' + props.index + ' Settings Configuration'}
        componentId={componentId}
        className={props.cx('refClkSettings')}
        symbolArray={props.RefClkSettingsSymbolArray}
        dialogWidth='50rem'
        dialogHeight='40rem'
      />
      <ResetSymbolsIcon
        tooltip={'RefClk ' + props.index + ' symbols to default value'}
        className={props.cx('refclkReset')}
        componentId={componentId}
        resetSymbolsArray={props.RefClkSettingsSymbolArray}
      />
      {/* <GetButton
        buttonDisplayText={'Auto Calculate'}
        className={props.cx('autoCalculateRefClk')}
        toolTip={'Press this to Auto-Calculate Reference Clock Frequency'}
        buttonClick={refClkAutoCalculationButtonClicked}
      /> */}
      <Dialog
        header='Reference Clock Divider and Trim Auto-Calculator'
        visible={dialogStatus}
        maximizable={true}
        onHide={() => {
          setDialogStatus(false);
        }}>
        <ReferenceAutoCalculation />
      </Dialog>
    </div>
  );
};
export default RefClkControllerBoxTemplate;
