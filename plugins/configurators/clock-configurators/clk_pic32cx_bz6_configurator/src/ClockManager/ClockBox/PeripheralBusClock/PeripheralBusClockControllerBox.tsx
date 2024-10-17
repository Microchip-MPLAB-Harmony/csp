import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import { InputTextarea } from 'primereact/inputtextarea';
import {
  CheckBoxDefault,
  InputNumberDefault,
  PluginConfigContext,
  useBooleanSymbol,
  useIntegerSymbol,
  useStringSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import React, { useContext } from 'react';
import { GetClockDisplayFreqValue } from 'clock-common/lib/Tools/Tools';
import FrequencyLabelComponent from 'clock-common/lib/Components/LabelComponent/FrequencyLabelComponent';

let maximumPeripheralFreq = 100000000;
const PeripheralBusClockControllerBox = (props: {
  tabTitle: string;
  componentId: string;
  cx: (...classNames: string[]) => string;
  pbclkSettingsSymbolArray: string[];
  pbclkController: ControlInterface[];
  peripheralHelp: string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const pbclkDiv = useIntegerSymbol({
    componentId,
    symbolId: 'CONFIG_SYS_CLK_PBDIV' + props.tabTitle
  });
  const pbclkEnable = useBooleanSymbol({
    componentId: componentId,
    symbolId: 'CONFIG_SYS_CLK_PBCLK' + props.tabTitle + '_ENABLE'
  });
  const pb3ClockFreqMaxRange = useIntegerSymbol({ componentId, symbolId: 'PBCLK3_FREQ_MAX' });
  const pb3ClockFreq = useStringSymbol({
    componentId,
    symbolId: 'CONFIG_SYS_CLK_PBCLK3_FREQ'
  });

  return (
    <div>
      <PlainLabel
        disPlayText={pbclkDiv.value + ''}
        className={props.cx('lbl_pbxdiv')}
      />
      <InputNumberDefault
        componentId={props.componentId}
        symbolId={'CONFIG_SYS_CLK_PBDIV' + props.tabTitle}
        className={props.cx('peripheralBusClkDiv1')}
      />
      <CheckBoxDefault
        componentId={props.componentId}
        symbolId={'CONFIG_SYS_CLK_PBCLK' + props.tabTitle + '_ENABLE'}
        className={props.cx('cb_pbclk_enable1')}
      />

      {pbclkEnable.value === true && (
        <FrequencyLabelComponent
          componentId={componentId}
          symbolId={'CONFIG_SYS_CLK_PBCLK' + props.tabTitle + '_FREQ'}
          // minMaxOutofRangeRedColorStatus={
          //   props.tabTitle === '3' && Number(pb3ClockFreq.value) > pb3ClockFreqMaxRange.value
          // }
          // tooltip={
          //   props.tabTitle === '3'
          //     ? 'Maximum frequency of PBCLK3 is ' +
          //       GetClockDisplayFreqValue(pb3ClockFreqMaxRange.value)
          //     : ''
          // }
          className={props.cx('pbclkxFreq')}
        />
      )}
      <PlainLabel
        disPlayText={props.tabTitle}
        booldStatus={true}
        className={props.cx('lbl_pbclkNum')}
      />
      <PlainLabel
        disPlayText={props.tabTitle}
        booldStatus={true}
        className={props.cx('lbl_pbclkx')}
      />
      <PlainLabel
        disPlayText={'To Peripherals:'}
        booldStatus={true}
        className={props.cx('lbl_To1')}
      />
      <InputTextarea
        value={props.peripheralHelp}
        className={props.cx('txt_pbclkPeripherals')}
      />
      <SettingsDialog
        tooltip={'pbclk ' + props.tabTitle + ' Settings Configuration'}
        componentId={props.componentId}
        className={props.cx('peripheralBusClock_Settings')}
        symbolArray={props.pbclkSettingsSymbolArray}
        dialogWidth='47rem'
        dialogHeight='25rem'
      />
      <ResetSymbolsIcon
        tooltip={'pbclk ' + props.tabTitle + ' symbols to default value'}
        className={props.cx('peripheralBusClock_reset')}
        componentId={props.componentId}
        resetSymbolsArray={props.pbclkSettingsSymbolArray}
      />
    </div>
  );
};
export default React.memo(PeripheralBusClockControllerBox);
