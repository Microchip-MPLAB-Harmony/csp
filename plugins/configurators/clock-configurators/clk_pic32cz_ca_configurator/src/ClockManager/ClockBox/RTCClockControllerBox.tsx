import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import { useContext, useState } from 'react';
import {
  KeyValueSetRadio,
  PluginConfigContext,
  useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import {
  getAllSymbolsFromJSON,
  getDynamicLabelsFromJSON
} from 'clock-common/lib/Tools/ClockJSONTools';
import LoadDynamicFreqencyLabels from 'clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels';

const RTCClockControllerBox = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const cmd_rtc = useKeyValueSetSymbol({
    componentId,
    symbolId: 'CONFIG_CLOCK_RTC_SRC'
  });

  const [allJsonSymbols] = useState<string[]>(getAllSymbolsFromJSON(props.clockController));

  const [dynamicSymbolLabelInfo] = useState(() => getDynamicLabelsFromJSON(props.clockController));

  return (
    <div>
      <LoadDynamicFreqencyLabels
        componentId={componentId}
        dynamicLabelSymbolsInfo={dynamicSymbolLabelInfo}
        redColorForZeroFrequency={true}
        cx={props.cx}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={cmd_rtc}
        classPrefix={'rtcClkRadio'}
        labelClassPrefix='rtcClkRadioName'
        classResolver={props.cx}
      />
      <ResetSymbolsIcon
        tooltip='Reset Clock symbols to default value'
        className={props.cx('rtcClkReset')}
        componentId={componentId}
        resetSymbolsArray={allJsonSymbols.concat('CONFIG_CLOCK_RTC_SRC')}
      />
    </div>
  );
};

export default RTCClockControllerBox;
