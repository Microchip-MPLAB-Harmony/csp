import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import {
  CheckBoxDefault,
  InputNumberDefault,
  KeyValueSetRadio,
  PluginConfigContext,
  useIntegerSymbol,
  useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import FrequencyLabelComponent from 'clock-common/lib/Components/LabelComponent/FrequencyLabelComponent';
import React, { useContext } from 'react';
import { getFreqSymbolId } from '../../MainBlock';

const PCKClockControllerBoxTemplate = (props: {
  tabTitle: string;
  componentId: string;
  cx: (...classNames: string[]) => string;
  clkSettingsSymbolArray: string[];
  clkController: ControlInterface[];
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const pckCss = useKeyValueSetSymbol({
    componentId,
    symbolId: 'CLK_PCK' + props.tabTitle + '_CSS'
  });
  const pckDiv = useIntegerSymbol({
    componentId,
    symbolId: 'CLK_PCK' + props.tabTitle + '_PRES'
  });

  return (
    <div>
      <PlainLabel
        disPlayText={props.tabTitle}
        booldStatus={true}
        className={props.cx('pckCount')}
      />
      <PlainLabel
        disPlayText={'(1+' + pckDiv.value + ')'}
        className={props.cx('lbl_pckx_pres')}
      />
      <InputNumberDefault
        componentId={props.componentId}
        symbolId={'CLK_PCK' + props.tabTitle + '_PRES'}
        className={props.cx('spn_pckx_pres')}
      />
      <CheckBoxDefault
        componentId={props.componentId}
        symbolId={'CLK_PCK' + props.tabTitle + '_EN'}
        className={props.cx('chk_pckx_en')}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={pckCss}
        classPrefix='pckClkRadio'
        labelClassPrefix='pckClkRadioName'
        classResolver={props.cx}
      />
      <FrequencyLabelComponent
        componentId={props.componentId}
        symbolId={'CLK_PCK' + props.tabTitle + '_FREQUENCY'}
        className={props.cx('lbl_pckx_pres_freq')}
      />
      <FrequencyLabelComponent
        componentId={props.componentId}
        symbolId={getFreqSymbolId(pckCss.selectedOptionPair?.key)}
        className={props.cx('lbl_pckx_css_freq')}
        redColorForZeroFrequency={true}
      />
      <SettingsDialog
        tooltip={'PCK clock ' + props.tabTitle + ' Settings Configuration'}
        componentId={props.componentId}
        className={props.cx('pcksettings')}
        symbolArray={props.clkSettingsSymbolArray}
        dialogWidth='45rem'
        dialogHeight='20rem'
      />
      <ResetSymbolsIcon
        tooltip={'PCK clock ' + props.tabTitle + ' symbols to default value'}
        className={props.cx('pckReset')}
        componentId={props.componentId}
        resetSymbolsArray={props.clkSettingsSymbolArray}
      />
    </div>
  );
};
export default React.memo(PCKClockControllerBoxTemplate);
