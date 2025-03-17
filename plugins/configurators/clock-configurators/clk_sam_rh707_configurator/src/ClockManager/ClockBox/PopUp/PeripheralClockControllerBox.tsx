import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import { useContext, useState } from 'react';
import { Button } from 'primereact/button';
import { Dialog } from 'primereact/dialog';
import PeripheralClockConfiguration from './PeripheralClockConfiguration';
import FrequencyLabelComponent from 'clock-common/lib/Components/LabelComponent/FrequencyLabelComponent';
import { PluginConfigContext, useComboSymbol } from '@mplab_harmony/harmony-plugin-client-lib';
import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';

const PeripheralClockControllerBox = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = "core" } = useContext(PluginConfigContext);
  const [periPheralPopup, setPeriPheralPopup] = useState(false);
  const gclk_ids = useComboSymbol({
    componentId,
    symbolId: 'GCLK_IO_CLOCK_CONFIG_UI'
  });
  let peripheralClockSymbolArray = createPeripheralSymbolsArray();
  function createPeripheralSymbolsArray() {
    let dataArr = [];
    for (let i = 0; i < gclk_ids.options.length; i++) {
      dataArr.push(gclk_ids.options[i] + "_CLOCK_ENABLE");
      dataArr.push(gclk_ids.options[i] + '_GCLK_ENABLE');
      dataArr.push(gclk_ids.options[i] + "_GCLK_CSS");
      dataArr.push(gclk_ids.options[i] + "_GCLK_DIV");
    }
    return dataArr;
  }
  return (
    <div>
      <FrequencyLabelComponent className={props.cx('rc2ck')} componentId={componentId} symbolId='CLK_RC2CK_FREQ'/>
      <FrequencyLabelComponent className={props.cx('mdslk')} componentId={componentId} symbolId='CLK_MD_SLCK_FREQ'/>
      <FrequencyLabelComponent className={props.cx('mainck')} componentId={componentId} symbolId='CLK_MAINCK_FREQ'/>
      <FrequencyLabelComponent className={props.cx('pllack')} componentId={componentId} symbolId='CLK_PLLACK_FREQ'/>
      <FrequencyLabelComponent className={props.cx('pllbck')} componentId={componentId} symbolId='CLK_PLLBCK_FREQ'/>
      <FrequencyLabelComponent className={props.cx('mck')} componentId={componentId} symbolId='CLK_MCK_FREQ'/>
      <Button
        label='Peripheral Clock Configuration'
        className={props.cx('clockConfigbtn')}
        onClick={() => setPeriPheralPopup(true)}
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
      <ResetSymbolsIcon
        tooltip='Reset Peripheral symbols to default value'
        className={props.cx('perCReset')}
        componentId={componentId}
        resetSymbolsArray={peripheralClockSymbolArray}
      />
    </div>
  );
};

export default PeripheralClockControllerBox;
