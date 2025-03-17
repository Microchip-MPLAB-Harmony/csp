import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import { useContext, useState } from 'react';
import { Button } from 'primereact/button';
import GclockIOConfiguration from './GclockIOConfiguration';
import { Dialog } from 'primereact/dialog';
import PeripheralClockConfiguration from './PeripheralClockConfiguration';
import { PluginConfigContext, useComboSymbol, useIntegerSymbol, useKeyValueSetSymbol } from '@mplab_harmony/harmony-plugin-client-lib';
import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';

const PeripheralClockControllerBox = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const [periPheralPopup, setPeriPheralPopup] = useState(false);
  const [genericPopup, setGenericPopup] = useState(false);
  const NumberofGenerators = useIntegerSymbol({ componentId, symbolId: 'GCLK_NUM_PADS' });
  const gclk_ids = useKeyValueSetSymbol({
    componentId,
    symbolId: 'GCLK_IO_CLOCK_CONFIG_UI'
  });
  let peripheralClockSymbolArray = createPeripheralSymbolsArray();
  function createPeripheralSymbolsArray() {
    let dataArr = [];
    for (let i = 0; i < gclk_ids.options.length; i++) {
      dataArr.push(gclk_ids.options[i] + '_CHEN');
      dataArr.push(gclk_ids.options[i] + '_GENSEL');
      dataArr.push(gclk_ids.options[i] + '_FREQ');
    }
    return dataArr;
  }
  let gclkSymbolArray = createGclockSymbolArray();
  function createGclockSymbolArray() {
    let dataArr = [];
    for (let i = 0; i < NumberofGenerators.value; i++) {
      dataArr.push('GCLK_' + i + '_OUTPUTENABLE');
      dataArr.push('GCLK_IN_' + i + '_FREQ');
      dataArr.push('GCLK_IO_' + i + '_FREQ');
    }
    return dataArr;
  }

  return (
    <div>
      <Button
        label='Peripheral Clock Configuration'
        className={props.cx('periClockConfig')}
        onClick={() => setPeriPheralPopup(true)}
      />
      <Button
        label='GCLK I/O Configuration'
        className={props.cx('gclkIOConfig')}
        onClick={() => setGenericPopup(true)}
      />
      <Dialog
        header='Peripheral Clock Configuration'
        visible={periPheralPopup}
        maximizable={true}
        onHide={() => {
          setPeriPheralPopup(false);
        }}>
        <PeripheralClockConfiguration />
      </Dialog>
      <Dialog
        header='GCLK I/O Configuration'
        visible={genericPopup}
        maximizable={true}
        onHide={() => {
          setGenericPopup(false);
        }}>
        <GclockIOConfiguration />
      </Dialog>
      <ResetSymbolsIcon
        tooltip='Reset Peripheral Clock Configuration symbols to default value'
        className={props.cx('peripheralClockSelectionReset')}
        componentId={componentId}
        resetSymbolsArray={peripheralClockSymbolArray}
      />
      <ResetSymbolsIcon
        tooltip='Reset GCLK I/O Configuration symbols to default value'
        className={props.cx('gclkIOReset')}
        componentId={componentId}
        resetSymbolsArray={gclkSymbolArray}
      />
    </div>
  );
};

export default PeripheralClockControllerBox;
