import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import { useContext } from 'react';
import {
  KeyValueSetRadio,
  PluginConfigContext,
  useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';

const SLCDControllerBox = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const cmd_rtc = useKeyValueSetSymbol({
    componentId,
    symbolId: 'CONFIG_CLOCK_SLCD_SRC'
  });
  return (
    <div>
      <KeyValueSetRadio
        keyValueSetSymbolHook={cmd_rtc}
        classPrefix={'scld_source'}
        labelClassPrefix='scld_sourceLabel'
        classResolver={props.cx}
      />
      <SettingsDialog
        tooltip='Clock Settings Configuration'
        componentId={componentId}
        className={props.cx('scldClksettings')}
        symbolArray={['CONFIG_CLOCK_SLCD_SRC']}
        dialogWidth='50rem'
        dialogHeight='27rem'
      />
      <ResetSymbolsIcon
        tooltip='Reset Clock symbols to default value'
        className={props.cx('scldClkReset')}
        componentId={componentId}
        resetSymbolsArray={['CONFIG_CLOCK_SLCD_SRC']}
      />
    </div>
  );
};

export default SLCDControllerBox;
