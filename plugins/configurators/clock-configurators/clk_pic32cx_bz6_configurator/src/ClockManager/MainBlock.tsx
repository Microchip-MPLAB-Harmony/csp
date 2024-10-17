import ClockPIC32CXBX from '../Resources/data/react_pic32cx_bz6.svg';
import positions from '../Resources/data/positions.module.css';
import styles from './block-diagram-view.module.css';
import tabCss from '../Styles/tab.module.css';
import ClockSamC20C21Json from '../Resources/data/controls.json';
import { useContext, useEffect, useState } from 'react';
import ControlInterfac from 'clock-common/lib/Tools/ControlInterface';
import { ConfirmDialog } from 'primereact/confirmdialog';
import SummaryPage from './Summary';
import SystemPLLControllerBox from './ClockBox/SystemPLLControllerBox';
import {
  createClassResolver,
  PluginConfigContext,
  PluginToolbar,
  usePannableContainer,
  useZoomableContainer
} from '@mplab_harmony/harmony-plugin-client-lib';
import { MenuItem } from 'primereact/menuitem';
import RefClockControllerXBox from './ClockBox/ReferenceClock/RefClockControllerXBox';
import PeripheralClockControllerBox from './ClockBox/PopUp/PeripheralClockControllerBox';
import EthernetController from './ClockBox/EtherNet/EthernetController';
import USBPLLController from './ClockBox/USBPLL/USBPLLController';
import PrimaryAndScondaryControllerBox from './ClockBox/PrimaryAndScondaryControllerBox';
import PeripheralBusClockController from './ClockBox/PeripheralBusClock/PeripheralBusClockController';
import CustomLogic from './ClockBox/CustomLogic/CustomLogic';

export let controlJsonData = ClockSamC20C21Json as ControlInterfac[];

export const cx = createClassResolver(positions, styles, tabCss);

const MainBlock = () => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const [summaryDialogVisible, setSummaryDialogVisible] = useState(false);

  const zoomableContainer = useZoomableContainer();
  const pannableContainer = usePannableContainer();

  useEffect(() => {}, []);

  const items: MenuItem[] = [
    // {
    //   label: 'Summary',
    //   icon: 'pi pi-fw pi-chart-bar',
    //   command: () => setSummaryDialogVisible(true)
    // },
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

  function getBoxControlData(boxId: string) {
    return controlJsonData.filter((e) => e.box_id === boxId);
  }
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
            src={ClockPIC32CXBX}
            alt='icon'
            className={cx('main-block-diagram')}
          />
          <EthernetController
            controllerData={getBoxControlData('ewPllControllerBox')}
            cx={cx}
          />
          <USBPLLController
            controllerData={getBoxControlData('usbPllControllerBox')}
            cx={cx}
          />
          <SystemPLLControllerBox
            systemPLLControllerData={getBoxControlData('systemPllControllerBox')}
            cx={cx}
          />
          <PrimaryAndScondaryControllerBox
            controller={getBoxControlData('pscontrollerbox')}
            cx={cx}
          />
          <RefClockControllerXBox
            refClockData={getBoxControlData('refClk0Box')}
            cx={cx}
          />
          <PeripheralClockControllerBox
            clockController={getBoxControlData('peripheralClkBox')}
            cx={cx}
          />
          <PeripheralBusClockController
            controller={getBoxControlData('peripheralBusClockBox')}
            cx={cx}
          />
          <CustomLogic cx={cx} />
        </div>
      </div>
    </>
  );
};
export default MainBlock;
