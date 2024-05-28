import { useContext, useState } from 'react';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';

import { ListBox } from 'primereact/listbox';
import PLLClkControllerBoxTemplate from './PLLClockControllerBoxTemplate';
import { getPLLClkSettingsSymbol } from './PLLClockSettingsSymbol';
import { PluginConfigContext, useBooleanSymbol } from '@mplab_harmony/harmony-plugin-client-lib';

interface Tab {
  name: string;
  status: string;
}

export const pllTabs: Tab[] = [
  { name: 'CPUPLL', status: 'CLK_CPUPLL_EN' },
  { name: 'SYSPLL', status: 'CLK_SYSPLL_EN' },
  { name: 'DDRPLL', status: 'CLK_DDRPLL_EN' },
  { name: 'GPUPLL', status: 'CLK_GPUPLL_EN' },
  { name: 'BAUDPLL', status: 'CLK_BAUDPLL_EN' },
  { name: 'AUDIOPLL', status: 'CLK_AUDIOPLL_EN' },
  { name: 'ETHPLL', status: 'CLK_ETHPLL_EN' },
  { name: 'LVDSPLL', status: 'CLK_LVDSPLL_EN' },
  { name: 'USBPLL', status: 'CLK_USBPLL_EN' }
];

const PLLClockControllerXBox = (props: {
  controller: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const [value, setValue] = useState<Tab | null>(pllTabs[0]);

  const tabTemplate = (option: any) => {
    // eslint-disable-next-line react-hooks/rules-of-hooks
    const PLLClocKEnable = useBooleanSymbol({
      componentId,
      symbolId: option.status
    });
    return (
      <div
        style={{ fontSize: '10px' }}
        className={PLLClocKEnable.value ? props.cx('enable') : props.cx('disable')}>
        {option.name}
      </div>
    );
  };

  return (
    <div>
      <div>
        <ListBox
          className={props.cx('pllControlTab')}
          value={value}
          options={pllTabs}
          optionLabel='name'
          itemTemplate={tabTemplate}
          onChange={(e) => setValue(e.value)}
        />
      </div>
      <PLLClkControllerBoxTemplate
        tabTitle={value?.name ? value.name : 'CPUPLL'}
        PLLClkSettingsSymbolArray={getPLLClkSettingsSymbol(value?.name ? value.name : 'CPUPLL')}
        PLLClkController={props.controller}
        componentId={componentId}
        cx={props.cx}
      />
    </div>
  );
};
export default PLLClockControllerXBox;
