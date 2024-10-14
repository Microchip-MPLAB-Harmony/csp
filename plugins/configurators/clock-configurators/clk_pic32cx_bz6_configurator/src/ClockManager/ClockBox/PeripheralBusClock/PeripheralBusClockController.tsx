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
  'PAC,FREQM,EIC,SERCOM0,SERCOM1,TC0,TC1,TC2,TC3,TC4,TC5,TC6,TC7,TCC0,TCC1,TCC2,PORTA,PORTB,PORTC,PORTD,PORTE,WDT,FC,PFW,CRU,DMT,PPS,ADC,CVD,DAC,ROT,QEI';
arrayPeripheralHelp[1] = 'CMCC,EVSYS,RAM_ECC,SERCOM6(I2C),CCL,AC,HMTX';
arrayPeripheralHelp[2] = 'RTCC,DSCO';
arrayPeripheralHelp[3] = 'SERCOM2,SERCOM3,SERCOM4,SERCOM5,TC8,TC9';
arrayPeripheralHelp[4] = 'Wireless ZBT';

export const PBCLKTabs: Tab[] = [
  { name: 'PBCLK 1', id: '1', status: 'CONFIG_SYS_CLK_PBCLK1_ENABLE' },
  { name: 'PBCLK 2', id: '2', status: 'CONFIG_SYS_CLK_PBCLK2_ENABLE' },
  { name: 'PBCLK 3', id: '3', status: 'CONFIG_SYS_CLK_PBCLK3_ENABLE' },
  { name: 'PBCLK 4', id: '4', status: 'CONFIG_SYS_CLK_PBCLK4_ENABLE' },
  { name: 'PBCLK 5', id: '5', status: 'CONFIG_SYS_CLK_PBCLK5_ENABLE' }
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
