import CLOCKSAMA7D6 from '../Resources/data/react_SAMA7D6_clock_new.svg';
import positions from '../Resources/data/positions.module.css';
import styles from './block-diagram-view.module.css';
import tabCss from '../Styles/tab.module.css';
import ClockSamC20C21Json from '../Resources/data/controls.json';
import { useContext, useEffect, useState } from 'react';
import ControlInterfac from 'clock-common/lib/Tools/ControlInterface';
import { ConfirmDialog } from 'primereact/confirmdialog';
import SlowClockControllerBox from './ClockBox/SlowClockControllerBox';
import {
  createClassResolver,
  PluginConfigContext,
  PluginToolbar,
  usePannableContainer,
  useZoomableContainer
} from '@mplab_harmony/harmony-plugin-client-lib';
import { MenuItem } from 'primereact/menuitem';
import MainClockControllerBox from './ClockBox/MainClockControllerBox';
import PLLClockControllerXBox from './ClockBox/PLLClock/PLLClockControllerXBox';
import ProcessClockControllerBox from './ClockBox/ProcessClock/ProcessClockControllerBox';
import MCKClockControllerXBox from './ClockBox/MCK/MCKClockControllerXBox';
import PCKClockControllerXBox from './ClockBox/PCK/PCKClockControllerXBox';
import PeripheralClockControllerBox from './ClockBox/PopUp/PeripheralClockControllerBox';
import SystemCounterControllerBox from './ClockBox/SystemCounterControllerBox';
import USBClockControllerBox from './ClockBox/USBClockControllerBox';
import { Dialog } from 'primereact/dialog';
import Summary from './Summary/Summary';

export let controlJsonData = ClockSamC20C21Json as ControlInterfac[];
export function getBoxControlData(boxId: string) {
  return controlJsonData.filter((e) => e.box_id === boxId);
}

const cx = createClassResolver(positions, styles, tabCss);

const MainBlock = () => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const [summaryDialogVisible, setSummaryDialogVisible] = useState(false);

  const zoomableContainer = useZoomableContainer();
  const pannableContainer = usePannableContainer();

  useEffect(() => {}, []);

  const items: MenuItem[] = [
    {
      label: 'Summary',
      icon: 'pi pi-fw pi-chart-bar',
      command: () => setSummaryDialogVisible(true)
    },
    {
      label: 'Zoom',
      icon: 'pi pi-search-plus',
      items: [
        {
          label: 'Zoom In (Alt + Scroll Up)',
          icon: 'pi pi-fw pi-search-plus',
          command: () => zoomableContainer.zoomIn()
        },
        {
          label: 'Reset Zoom (Alt + Scroll Click)',
          icon: 'pi pi-fw pi-refresh',
          command: () => zoomableContainer.resetZoom()
        },
        {
          label: 'Zoom Out (Alt + Scroll Down)',
          icon: 'pi pi-fw pi-search-minus',
          command: () => zoomableContainer.zoomOut()
        }
      ]
    }
  ];

  return (
    <>
      <ConfirmDialog />
      <PluginToolbar
        menuItems={items}
        title='Clock Configurator'
      />
      <div
        className={cx('pannable-container')}
        ref={pannableContainer.ref}
        {...pannableContainer.props}>
        <div
          className={cx('svg-container')}
          ref={zoomableContainer.ref}
          {...zoomableContainer.props}>
          <img
            src={CLOCKSAMA7D6}
            alt='icon'
            className={cx('main-block-diagram')}
          />
          <SlowClockControllerBox
            slowClockController={getBoxControlData('slowClockBox')}
            cx={cx}
          />
          <MainClockControllerBox
            controller={getBoxControlData('mainClkBox')}
            cx={cx}
          />
          <PLLClockControllerXBox
            controller={getBoxControlData('pllControlBox')}
            cx={cx}
          />
          <ProcessClockControllerBox
            controller={getBoxControlData('processClockBox')}
            cx={cx}
          />
          <MCKClockControllerXBox
            controller={getBoxControlData('mckClkBox')}
            cx={cx}
          />
          <PCKClockControllerXBox
            controller={getBoxControlData('pckClkBox')}
            cx={cx}
          />
          <PeripheralClockControllerBox
            clockController={getBoxControlData('peripheralClkBox')}
            cx={cx}
          />
          <SystemCounterControllerBox
            clockController={getBoxControlData('systemCounterControllerBox')}
            cx={cx}
          />
          <USBClockControllerBox
            slowClockController={getBoxControlData('usbControlBox')}
            cx={cx}
          />
        </div>
        <Dialog
          header='Clock Summary'
          visible={summaryDialogVisible}
          maximizable={true}
          onHide={() => {
            setSummaryDialogVisible(!summaryDialogVisible);
          }}>
          <Summary />
        </Dialog>
      </div>
    </>
  );
};
export default MainBlock;

export const getFreqSymbolId = (selectedValue: any) => {
  let sym = 'MD_SLOW_CLK_FREQUENCY';
  if (
    selectedValue === 'MD_SCLK' ||
    selectedValue === 'MD_SLOW_CLK' ||
    selectedValue === 'SLOW_CLK'
  ) {
    sym = 'MD_SLOW_CLK_FREQUENCY';
  } else if (selectedValue === 'TD_SLOW_CLK' || selectedValue === 'TD_SLOW_CLOCK') {
    sym = 'TD_SLOW_CLOCK_FREQUENCY';
  } else if (selectedValue === 'MAINCK' || selectedValue === 'MAIN_CLK') {
    sym = 'MAINCK_FREQUENCY';
  } else if (selectedValue === 'SYSPLL' || selectedValue === 'SYSPLLCK') {
    sym = 'SYSPLL_FREQUENCY';
  } else if (selectedValue === 'MCK0') {
    sym = 'MCK0_FREQUENCY';
  } else if (selectedValue === 'DDRPLL') {
    sym = 'DDRPLL_FREQUENCY';
  } else if (selectedValue === 'CPUPLLCK') {
    sym = 'CPUPLL_FREQUENCY';
  } else if (selectedValue === 'GPUPLL') {
    sym = 'GPUPLL_FREQUENCY';
  } else if (selectedValue === 'BAUDPLL') {
    sym = 'BAUDPLL_FREQUENCY';
  } else if (selectedValue === 'AUDIOPLL') {
    sym = 'AUDIOPLL_FREQUENCY';
  } else if (selectedValue === 'ETHPLL') {
    sym = 'ETHPLL_FREQUENCY';
  } else if (selectedValue === 'USBPLL') {
    sym = 'USBPLL_FREQUENCY';
  }
  return sym;
};
