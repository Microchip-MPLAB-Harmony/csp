import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import { useContext } from 'react';
import { CheckBoxDefault, PluginConfigContext } from '@mplab_harmony/harmony-plugin-client-lib';
import FrequencyLabelComponent from 'clock-common/lib/Components/LabelComponent/FrequencyLabelComponent';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';

const SystemCounterControllerBox = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  return (
    <div>
      <CheckBoxDefault
        componentId={componentId}
        symbolId={'SYSTEM_COUNTER_ENABLE'}
        className={props.cx('chk_tmpgn_en')}
      />
      <FrequencyLabelComponent
        componentId={componentId}
        symbolId={'SYSTEM_COUNTER_FREQUENCY'}
        className={props.cx('lbl_tmpgn_freq')}
      />
      <SettingsDialog
        tooltip='System Counter Settings Configuration'
        componentId={componentId}
        className={props.cx('systemCounterSettings')}
        symbolArray={['SYSTEM_COUNTER_ENABLE', 'SYSTEM_COUNTER_FREQUENCY']}
        dialogWidth='40rem'
        dialogHeight='20rem'
      />
      <ResetSymbolsIcon
        tooltip='System Counter symbols to default value'
        className={props.cx('systemCounterReset')}
        componentId={componentId}
        resetSymbolsArray={['SYSTEM_COUNTER_ENABLE', 'SYSTEM_COUNTER_FREQUENCY']}
      />
    </div>
  );
};

export default SystemCounterControllerBox;
