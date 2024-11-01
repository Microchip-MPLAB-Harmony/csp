import { useContext, useState } from 'react';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';

import { ListBox } from 'primereact/listbox';
import { PluginConfigContext, useBooleanSymbol } from '@mplab_harmony/harmony-plugin-client-lib';
import { getPeripheralBusClockSymbols } from './PeripheralBusClocKSymbols';
import PeripheralBusClockControllerBox from './PeripheralBusClockControllerBox';

interface Tab {
  name: string;
  id: string;
  status: string;
}
let arrayPeripheralHelp: string[] = [];
arrayPeripheralHelp[0] =
  'ADC, CRU, DMT, EIC, FREQM, NVM, PAC, PFW, PORTA, PORTB, PPS, SERCOM-0, SERCOM-1,' +
  ' CVD, ROT, DAC_CTRL, TC-0, TC-1, TC-2, TC-3, TC-4, TC-5, TC-6, TC-7, TCC-0, TCC-1, TCC-2, WDT';
arrayPeripheralHelp[1] = 'AC, CCL, CMCC, DMAC, DSU, EVSY, HMTX, QSPI, RAM ECC, SERCOM-2';
arrayPeripheralHelp[2] = 'DSCN, RTCC';

export const PBCLKTabs: Tab[] = [
  { name: 'PBCLK 1', id: '1', status: 'CONFIG_SYS_CLK_PBCLK1_ENABLE' },
  { name: 'PBCLK 2', id: '2', status: 'CONFIG_SYS_CLK_PBCLK2_ENABLE' },
  { name: 'PBCLK 3', id: '3', status: 'CONFIG_SYS_CLK_PBCLK3_ENABLE' }
];

const PeripheralBusClockController = (props: {
  controller: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const [value, setValue] = useState<Tab | null>(PBCLKTabs[0]);

  const tabTemplate = (option: any) => {
    // eslint-disable-next-line react-hooks/rules-of-hooks
    const PBCLKClocKEnable = useBooleanSymbol({
      componentId,
      symbolId: option.status
    });
    return (
      <div
        style={{ fontSize: '10px' }}
        className={PBCLKClocKEnable.value ? props.cx('enable') : props.cx('disable')}>
        {option.name}
      </div>
    );
  };
  return (
    <div>
      <div>
        <ListBox
          className={props.cx('tabPane_pb')}
          value={value}
          options={PBCLKTabs}
          optionLabel='name'
          itemTemplate={tabTemplate}
          onChange={(e) => setValue(e.value)}
        />
      </div>
      <PeripheralBusClockControllerBox
        tabTitle={value?.name ? value.id : '1'}
        pbclkSettingsSymbolArray={getPeripheralBusClockSymbols(value?.name ? value.id : '1')}
        pbclkController={props.controller}
        componentId={componentId}
        cx={props.cx}
        peripheralHelp={arrayPeripheralHelp[Number(value?.name ? value.id : '1') - 1]}
      />
    </div>
  );
};
export default PeripheralBusClockController;
