import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import { useContext } from 'react';
import {
  CheckBoxDefault,
  InputNumber,
  InputNumberDefault,
  PluginConfigContext,
  useBooleanSymbol,
  useIntegerSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import FrequencyLabelComponent from 'clock-common/lib/Components/LabelComponent/FrequencyLabelComponent';
import React from 'react';

const PLLClockControllerBoxTemplate = (props: {
  tabTitle: string;
  componentId: string;
  cx: (...classNames: string[]) => string;
  PLLClkSettingsSymbolArray: string[];
  PLLClkController: ControlInterface[];
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const coreFrequency = useIntegerSymbol({
    componentId,
    symbolId: props.tabTitle + '_CORE_FREQUENCY'
  });
  const divPMC = useIntegerSymbol({
    componentId,
    symbolId: 'CLK_' + props.tabTitle + '_DIVPMC'
  });
  const audioDivio = useIntegerSymbol({
    componentId,
    symbolId: 'CLK_AUDIOPLL_DIVIO'
  });
  const audioENIO = useBooleanSymbol({
    componentId,
    symbolId: 'CLK_AUDIOPLL_ENIOPLLCK'
  });

  return (
    <div>
      <PlainLabel
        disPlayText={props.tabTitle}
        booldStatus={true}
        className={props.cx('pllSelected')}
      />
      <PlainLabel
        disPlayText={
          props.tabTitle === 'LVDSPLL'
            ? '7*(' + divPMC.value + ' + 1)'
            : props.tabTitle === 'USBPLL'
            ? '2'
            : '(' + divPMC.value + ' + 1)'
        }
        className={props.cx('tab_PLLA_label_PLLDivPmc0')}
      />
      <PlainLabel
        disPlayText={'(' + audioDivio.value + ' + 1)'}
        className={props.cx('tab_label_PLLA_PLLDivpmc1')}
      />
      {props.tabTitle !== 'USBPLL' && (
        <PlainLabel
          disPlayText={'DIVPMC'}
          className={props.cx('pllDivPICLabel')}
        />
      )}
      <InputNumberDefault
        componentId={componentId}
        symbolId={'CLK_' + props.tabTitle + '_MUL'}
        className={props.cx('tab_PLLA_spinner_mul')}
      />
      <InputNumberDefault
        componentId={componentId}
        symbolId={'CLK_' + props.tabTitle + '_FRACR'}
        className={props.cx('tab_PLLA_spinner_fracr')}
      />
      <InputNumber
        integerSymbolHook={divPMC}
        className={props.cx('tab_PLLA_spinner_divpmc0')}
        hidden={false}
      />
      <CheckBoxDefault
        componentId={componentId}
        symbolId={'CLK_' + props.tabTitle + '_EN'}
        className={props.cx('tab_PLLA_checkBox_enpllo0')}
      />
      <CheckBoxDefault
        componentId={componentId}
        symbolId={'CLK_' + props.tabTitle + '_SS'}
        className={props.cx('tab_PLLA_checkBox_enspread')}
      />
      <InputNumberDefault
        componentId={componentId}
        symbolId={'CLK_' + props.tabTitle + '_SS_STEP'}
        className={props.cx('tab_PLLA_spinner_step')}
      />
      <InputNumberDefault
        componentId={componentId}
        symbolId={'CLK_' + props.tabTitle + '_SS_NSTEP'}
        className={props.cx('tab_PLLA_spinner_nstep')}
      />
      <FrequencyLabelComponent
        componentId={componentId}
        symbolId={props.tabTitle + '_CORE_FREQUENCY'}
        className={props.cx('lbl_pll_calc_freq')}
        minMaxOutofRangeRedColorStatus={
          coreFrequency.value < 600000000 || coreFrequency.value > 1000000000
        }
        tooltip={props.tabTitle + ' core frequency has to be lower than 1 GHz'}
      />
      <FrequencyLabelComponent
        componentId={componentId}
        symbolId={props.tabTitle + '_CORE_FREQUENCY'}
        className={props.cx('lbl_pll_calc_freq1')}
        minMaxOutofRangeRedColorStatus={
          coreFrequency.value < 600000000 || coreFrequency.value > 1000000000
        }
        tooltip={props.tabTitle + ' core frequency has to be lower than 1 GHz'}
      />
      <FrequencyLabelComponent
        componentId={componentId}
        symbolId={props.tabTitle + '_FREQUENCY'}
        className={props.cx('label_sym_PLLACK0_FREQUENCY')}
      />
      <InputNumberDefault
        componentId={componentId}
        symbolId={'CLK_AUDIOPLL_DIVIO'}
        disabled={props.tabTitle !== 'AUDIOPLL' ? true : audioDivio.readOnly}
        className={props.cx('tab_PLLA_spinner_divpmc1')}
      />
      <CheckBoxDefault
        componentId={componentId}
        symbolId={'CLK_AUDIOPLL_ENIOPLLCK'}
        disabled={props.tabTitle !== 'AUDIOPLL' ? true : audioENIO.readOnly}
        className={props.cx('tab_PLLA_checkBox_enpllo1')}
      />
      {props.tabTitle === 'AUDIOPLL' && (
        <FrequencyLabelComponent
          componentId={componentId}
          symbolId={'AUDIOPLL_IO_FREQUENCY'}
          className={props.cx('lbl_pll_divio_freq')}
        />
      )}
      <SettingsDialog
        tooltip={'PLLclock ' + props.tabTitle + ' Settings Configuration'}
        componentId={componentId}
        className={props.cx('Pll_settings')}
        symbolArray={props.PLLClkSettingsSymbolArray}
        dialogWidth='45rem'
        dialogHeight='40rem'
      />
      <ResetSymbolsIcon
        tooltip={'PLLClk ' + props.tabTitle + ' symbols to default value'}
        className={props.cx('Pll_reset')}
        componentId={componentId}
        resetSymbolsArray={props.PLLClkSettingsSymbolArray}
      />
    </div>
  );
};
export default React.memo(PLLClockControllerBoxTemplate);
