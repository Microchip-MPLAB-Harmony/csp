import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import { useContext, useState } from 'react';
import {
  KeyValueSetRadio,
  PluginConfigContext,
  useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import LoadDynamicFreqencyLabels from 'clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels';
import {
  getAllSymbolsFromJSON,
  getDynamicLabelsFromJSON
} from 'clock-common/lib/Tools/ClockJSONTools';
import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';

const RTCClockController = (props: {
  cx: (...classNames: string[]) => string;
  rtcClockController: ControlInterface[];
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const rtcSymbolHook = useKeyValueSetSymbol({ componentId, symbolId: 'CONFIG_CLOCK_RTC_SRC' });

  const [allJsonSymbols] = useState<string[]>(getAllSymbolsFromJSON(props.rtcClockController));
  const [dynamicLabelSymbolInfo] = useState(() =>
    getDynamicLabelsFromJSON(props.rtcClockController)
  );
  return (
    <div>
      <LoadDynamicFreqencyLabels
        componentId={componentId}
        dynamicLabelSymbolsInfo={dynamicLabelSymbolInfo}
        cx={props.cx}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={rtcSymbolHook}
        classPrefix={'rtcClockSelRadio'}
        labelClassPrefix={'rtcClockSelRadioName'}
        classResolver={props.cx}
      />
      {/* <SettingsDialog
        tooltip='RTC Clock Selection Settings'
        componentId={componentId}
        className={props.cx('rtcSettings')}
        symbolArray={allJsonSymbols}
        dialogWidth='50rem'
        dialogHeight='30rem'
      /> */}
      <ResetSymbolsIcon
        tooltip='Reset RTC Clock symbols to default value'
        className={props.cx('rtcClkSelectionReset')}
        componentId={componentId}
        resetSymbolsArray={allJsonSymbols}
      />
    </div>
  );
};
export default RTCClockController;
