import { useContext, useState, useCallback } from 'react';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import { ListBox } from 'primereact/listbox';
import { PluginConfigContext } from '@mplab_harmony/harmony-plugin-client-lib';
import GCKLClockControllerBoxTemplate from './GCKLClockControllerBoxTemplate';

interface Tab {
  name: string;
  id: string;
  status: string;
}

const GCLKTabs: Tab[] = [
  { name: 'PCLK 0', id: '0', status: 'GCLK_INST_NUM2' },
  { name: 'PCLK 1', id: '1', status: 'GCLK_INST_NUM3' },
];

const getGclockSymbols = (index: string) => [
  `CLK_PCK${index}_CSS`,
  `CLK_PCK${index}_PRES`,
  `CLK_PCK${index}_EN`,
];

const GclkXControllerBox = ({ controller, cx }: {
  controller: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const [value, setValue] = useState<Tab>(GCLKTabs[0]);

  const handleTabChange = useCallback((e: any) => {
    if (e.value !== null) setValue(e.value);
  }, []);

  const tabTemplate = useCallback((option: Tab) => (
    <div style={{ fontSize: '10px' }}>{option.name}</div>
  ), []);

  return (
    <div>
      <ListBox
        className={cx('pclkTabPane')}
        value={value}
        options={GCLKTabs}
        optionLabel="name"
        itemTemplate={tabTemplate}
        onChange={handleTabChange}
      />
      <GCKLClockControllerBoxTemplate
        tabTitle={value?.name ? value.id : '0'}
        gclkSettingsSymbolArray={getGclockSymbols(value.id)}
        gclkController={controller}
        componentId={componentId}
        cx={cx}
      />
    </div>
  );
};

export default GclkXControllerBox;
