import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import LoadDynamicComponents from 'clock-common/lib/Components/LoadDynamicComponents';
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
import FreqencyLabels from 'clock-common/lib/Components/LabelComponent/FreqencyLabels';

const MainClockControllerBox = (props: {
  controller: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const cmb_mainClock_sel_ = useKeyValueSetSymbol({
    componentId,
    symbolId: 'CLK_MOSCSEL'
  });

  const [allJsonSymbols] = useState<string[]>(getAllSymbolsFromJSON(props.controller));
  const [dynamicSymbolInfo] = useState(() => getDynamicSymbolsFromJSON(props.controller));
  const [dynamicLabelSymbolInfo] = useState(() => getDynamicLabelsFromJSON(props.controller));

  return (
    <div>
      <LoadDynamicComponents
        componentId={componentId}
        boxInfo={dynamicSymbolInfo}
        cx={props.cx}
      />
      <FreqencyLabels
        componentId={componentId}
        boxInfo={dynamicLabelSymbolInfo}
        cx={props.cx}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={cmb_mainClock_sel_}
        classPrefix='mainClkR'
        classResolver={props.cx}
      />
      <SettingsDialog
        tooltip='Main Clock Settings Configuration'
        componentId={componentId}
        className={props.cx('mainClk_settings')}
        symbolArray={allJsonSymbols}
        dialogWidth='40rem'
        dialogHeight='25rem'
      />
      <ResetSymbolsIcon
        tooltip='Main Slow Clock symbols to default value'
        className={props.cx('mainClk_reset')}
        componentId={componentId}
        resetSymbolsArray={allJsonSymbols}
      />
    </div>
  );
};

export default MainClockControllerBox;
