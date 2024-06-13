import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import LoadDynamicComponents from 'clock-common/lib/Components/LoadDynamicComponents';
import { useContext, useState } from 'react';
import {
  KeyValueSetRadio,
  PluginConfigContext,
  useIntegerSymbol,
  useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import {
  getAllSymbolsFromJSON,
  getDynamicSymbolsFromJSON
} from 'clock-common/lib/Tools/ClockJSONTools';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';

const USBClockControllerBox = (props: {
  slowClockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const source = useKeyValueSetSymbol({
    componentId,
    symbolId: 'CLK_USB_USBS'
  });
  const usbDiv = useIntegerSymbol({
    componentId,
    symbolId: 'CLK_USB_USBDIV'
  });

  const [allJsonSymbols] = useState<string[]>(getAllSymbolsFromJSON(props.slowClockController));
  const [dynamicSymbolInfo] = useState(() => getDynamicSymbolsFromJSON(props.slowClockController));

  return (
    <div>
      <LoadDynamicComponents
        componentId={componentId}
        boxInfo={dynamicSymbolInfo}
        cx={props.cx}
      />
      <PlainLabel
        disPlayText={'(' + usbDiv.value + '+1)'}
        className={props.cx('usbDivLabel')}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={source}
        classPrefix='usbRadio'
        labelClassPrefix='usbRadioName'
        classResolver={props.cx}
      />
      <SettingsDialog
        tooltip='USB Clock Settings Configuration'
        componentId={componentId}
        className={props.cx('usbSettings')}
        symbolArray={allJsonSymbols.concat(source.symbolId)}
        dialogWidth='40rem'
        dialogHeight='20rem'
      />
      <ResetSymbolsIcon
        tooltip='USB Slow Clock symbols to default value'
        className={props.cx('usbReset')}
        componentId={componentId}
        resetSymbolsArray={allJsonSymbols.concat(source.symbolId)}
      />
    </div>
  );
};

export default USBClockControllerBox;
