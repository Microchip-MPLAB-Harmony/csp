import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import {
  DropDownDefault,
  KeyValueSetRadio,
  PluginConfigContext,
  useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import React, { useContext } from 'react';
import { getFreqSymbolId } from '../../MainBlock';
import FrequencyLabelComponent from 'clock-common/lib/Components/LabelComponent/FrequencyLabelComponent';

const MCKClockControllerBoxTemplate = (props: {
  tabTitle: string;
  componentId: string;
  cx: (...classNames: string[]) => string;
  clkSettingsSymbolArray: string[];
  clkController: ControlInterface[];
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const mckCss = useKeyValueSetSymbol({
    componentId,
    symbolId: 'CLK_MCR_MCK' + props.tabTitle + '_CSS'
  });
  const mckDiv = useKeyValueSetSymbol({
    componentId,
    symbolId: 'CLK_MCR_MCK' + props.tabTitle + '_DIV'
  });

  return (
    <div>
      <PlainLabel
        disPlayText={props.tabTitle}
        booldStatus={true}
        className={props.cx('mckCount')}
      />
      <PlainLabel
        disPlayText={mckDiv.options[mckDiv.value]?.replaceAll('MASTER_DIV', '')}
        className={props.cx('mckClk0DivLabel')}
      />
      <DropDownDefault
        componentId={props.componentId}
        symbolId={'CLK_MCR_MCK' + props.tabTitle + '_DIV'}
        className={props.cx('cmb_mckx_css')}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={mckCss}
        classResolver={props.cx}
        classPrefix={'mckRadio'}
        labelClassPrefix='mckRadioName'
      />

      <FrequencyLabelComponent
        componentId={props.componentId}
        symbolId={'MCK' + props.tabTitle + '_FREQUENCY'}
        className={props.cx('mckClk0Freq')}
      />
      <FrequencyLabelComponent
        componentId={props.componentId}
        symbolId={getFreqSymbolId(mckCss.selectedOptionPair?.key)}
        className={props.cx('lbl_mckx_css_freq')}
        redColorForZeroFrequency={true}
      />

      <SettingsDialog
        tooltip={'MCC clock ' + props.tabTitle + ' Settings Configuration'}
        componentId={props.componentId}
        className={props.cx('mckSettings')}
        symbolArray={props.clkSettingsSymbolArray}
        dialogWidth='45rem'
        dialogHeight='20rem'
      />
      <ResetSymbolsIcon
        tooltip={'MCC clock ' + props.tabTitle + ' symbols to default value'}
        className={props.cx('mckReset')}
        componentId={props.componentId}
        resetSymbolsArray={props.clkSettingsSymbolArray}
      />
    </div>
  );
};
export default React.memo(MCKClockControllerBoxTemplate);
