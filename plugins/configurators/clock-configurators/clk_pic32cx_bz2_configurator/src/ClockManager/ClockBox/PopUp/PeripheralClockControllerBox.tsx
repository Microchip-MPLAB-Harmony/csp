import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import { useContext, useState } from 'react';
import { Button } from 'primereact/button';
import PeripheralsConfiguration from './PeripheralsConfiguration';
import { Dialog } from 'primereact/dialog';
import {
  BooleanSymbol,
  PluginConfigContext,
  StringSymbol,
  useIntegerSymbol,
  useSymbols
} from '@mplab_harmony/harmony-plugin-client-lib';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import { GetClockDisplayFreqValue } from 'clock-common/lib/Tools/Tools';

export const getRefClockIds = (suffix: string) => {
  let a: string[] = [];
  for (let i = 1; i < 7; i++) {
    a.push('CONFIG_SYS_CLK_REFCLK' + i + suffix);
  }
  return a;
};
const enableSymbolArray = getRefClockIds('_ENABLE');
const stringSymbolArray = getRefClockIds('_FREQ');

const PeripheralClockControllerBox = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const [periPheralPopup, setPeriPheralPopup] = useState(false);

  const enableSymbolsHooks = useSymbols({
    componentId: componentId,
    symbolIds: enableSymbolArray
  }) as BooleanSymbol[];
  const stringSymbolsHooks = useSymbols({
    componentId: componentId,
    symbolIds: stringSymbolArray
  }) as StringSymbol[];

  const freq7 = useIntegerSymbol({
    componentId,
    symbolId: 'LPCLK_FREQ'
  });

  return (
    <div>
      <Button
        label='Peripheral Clock Configuration'
        className={props.cx('periClockConfig')}
        onClick={() => setPeriPheralPopup(true)}
      />
      <PlainLabel
        disPlayText={GetClockDisplayFreqValue(freq7.value)}
        className={props.cx('lbl_lpck_1Freq')}
      />
      {enableSymbolsHooks.length !== 0 &&
        stringSymbolsHooks.length !== 0 &&
        enableSymbolsHooks.map((id, index) => (
          <PlainLabel
            key={index}
            disPlayText={
              enableSymbolsHooks[index].value
                ? GetClockDisplayFreqValue(Number(stringSymbolsHooks[index].value))
                : '0 Hz'
            }
            className={props.cx('lbl_refClk' + index + 'Freq')}
          />
        ))}

      <Dialog
        header='Peripheral Clock Configuration'
        visible={periPheralPopup}
        maximizable={true}
        onHide={() => {
          setPeriPheralPopup(false);
        }}>
        <PeripheralsConfiguration />
      </Dialog>
    </div>
  );
};

export default PeripheralClockControllerBox;
