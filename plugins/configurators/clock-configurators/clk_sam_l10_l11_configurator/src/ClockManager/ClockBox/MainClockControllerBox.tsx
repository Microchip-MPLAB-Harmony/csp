import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import LoadDynamicComponents from 'clock-common/lib/Components/Dynamic/LoadDynamicComponents';
import { useContext, useState } from 'react';
import {
  KeyValueSetRadio,
  PluginConfigContext,
  useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import {
  getAllSymbolsFromJSON,
  getDynamicLabelsFromJSON,
  getDynamicSymbolsFromJSON
} from 'clock-common/lib/Tools/ClockJSONTools';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import LoadDynamicFreqencyLabels from 'clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels';

const MainClockControllerBox = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const cmd_div1 = useKeyValueSetSymbol({
    componentId,
    symbolId: 'CONF_CPU_CLOCK_DIVIDER'
  });
  const cpuDivider = useKeyValueSetSymbol({
    componentId,
    symbolId: 'MCLK_SRC'
  });

  const [allJsonSymbols] = useState<string[]>(getAllSymbolsFromJSON(props.clockController));

  const [dynamicSymbolInfo] = useState(() => getDynamicSymbolsFromJSON(props.clockController));
  const [dynamicSymbolLabelInfo] = useState(() => getDynamicLabelsFromJSON(props.clockController));

  return (
    <div>
      <LoadDynamicComponents
        componentId={componentId}
        dynamicSymbolsInfo={dynamicSymbolInfo}
        cx={props.cx}
      />
      <LoadDynamicFreqencyLabels
        componentId={componentId}
        dynamicLabelSymbolsInfo={dynamicSymbolLabelInfo}
        redColorForZeroFrequency={true}
        cx={props.cx}
      />
      <PlainLabel
        disPlayText={'' + cmd_div1.selectedOption.replace('DIV', '')}
        className={props.cx('mclk0CPUDIVLabel')}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={cpuDivider}
        classPrefix="cpuDivider"
        classResolver={props.cx}
      />
      <SettingsDialog
        tooltip='Clock Settings Configuration'
        componentId={componentId}
        className={props.cx('mainClksettings')}
        symbolArray={allJsonSymbols}
        dialogWidth='50rem'
        dialogHeight='27rem'
      />
      <ResetSymbolsIcon
        tooltip='Reset Clock symbols to default value'
        className={props.cx('mainClkReset')}
        componentId={componentId}
        resetSymbolsArray={allJsonSymbols}
      />
    </div>
  );
};

export default MainClockControllerBox;
