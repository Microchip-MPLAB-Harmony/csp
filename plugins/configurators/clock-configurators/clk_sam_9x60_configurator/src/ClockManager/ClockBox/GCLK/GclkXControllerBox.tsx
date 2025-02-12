import { useContext, useState } from 'react';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';

import { ListBox } from 'primereact/listbox';
import { PluginConfigContext } from '@mplab_harmony/harmony-plugin-client-lib';
import GCKLClockControllerBoxTemplate from './GCKLClockControllerBoxTemplate';

interface Tab {
  name: string;
  id: string;
  status: string;
}

export const GCLKTabs: Tab[] = [
  { name: 'PCLK 0', id: '0', status: 'GCLK_INST_NUM2' },
  { name: 'PCLK 1', id: '1', status: 'GCLK_INST_NUM3' },
];
export const getGclockSymbols = (index: string) => {
  let symbols = [
    "CLK_PCK" + index + "_CSS",
    "CLK_PCK" + index + "_PRES",
    "CLK_PCK" + index + "_EN"
  ];
  return symbols;
};
const GclkXControllerBox = (props: {
  controller: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const [value, setValue] = useState<Tab>(GCLKTabs[0]);

  const tabTemplate = (option: any) => {
    return (
      <div
        style={{ fontSize: '10px' }}>
        {option.name}
      </div>
    );
  };
  return (
    <div>
      <div>
        <ListBox
          className={props.cx('pclkTabPane')}
          value={value}
          options={GCLKTabs}
          optionLabel='name'
          itemTemplate={tabTemplate}
          onChange={(e) => setValue(e.value)}
        />
      </div>
      <GCKLClockControllerBoxTemplate
        tabTitle={value?.name ? value.id : '0'}
        gclkSettingsSymbolArray={getGclockSymbols(value.id)}
        gclkController={props.controller}
        componentId={componentId}
        cx={props.cx}
      />
    </div>
  );
};
export default GclkXControllerBox;
