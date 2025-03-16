import { ReactComponent as ClockSAMC20C21 } from '../Resources/data/react_SAMC21.svg';
import positions from '../Resources/data/positions.module.css';
import styles from './block-diagram-view.module.css';
import tabCss from '../Styles/tab.module.css';
import ClockSamC20C21Json from '../Resources/data/controls.json';
import { useEffect, useState } from 'react';
import OscillatorsControllerBox from './ClockBox/Oscillators48MHzControllerBox';
import { ConfirmDialog } from 'primereact/confirmdialog';
import FDPLLController from './ClockBox/FDPLL/FDPLLController';
import Oscillators32KHzControllerBox from './ClockBox/Oscillators32KHzControllerBox';
import RTCClockController from './ClockBox/RTCClockController';
import MainClockController from './ClockBox/MainClockController';
import { MenuItem } from 'primereact/menuitem';
import {
  createClassResolver,
  PluginToolbar,
  usePannableContainer,
  useZoomableContainer
} from '@mplab_harmony/harmony-plugin-client-lib';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import useWindowDimensions from './Tools/WindowSize';
import Gclk0ControllerBox from './ClockBox/GCLK/Gclk0ControllerBox';
import Gclk1ControllerBox from './ClockBox/GCLK/Gclk1ControllerBox';
import GclkXControllerBox from './ClockBox/GCLK/GclkXControllerBox';
import PeripheralClockControllerBox from './ClockBox/PopUp/PeripheralClockControllerBox';
import { initializeSVG } from './Tools/SVGhandler';

export let controlJsonData = ClockSamC20C21Json as ControlInterface[];
export const cx = createClassResolver(positions, styles, tabCss);
const MainBlock = () => {
  const [summaryDialogVisible, setSummaryDialogVisible] = useState(false);

  const zoomableContainer = useZoomableContainer();
  const pannableContainer = usePannableContainer();

  const { height, width } = useWindowDimensions();

  useEffect(() => {
    console.log(height, width);
  }, [height, width]);
  useEffect(() => {
    initializeSVG(cx);
  }, []);

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

  try {
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
            <ClockSAMC20C21 id='clk_sam_c20_c21-main-image'></ClockSAMC20C21>
            <OscillatorsControllerBox
              oscillatorData={getBoxControlData('oscillatorsControllerBox')}
              cx={cx}
            />

            <FDPLLController
              fdpllControllerData={getBoxControlData('fdpllControllerBox')}
              cx={cx}
            />
            <Oscillators32KHzControllerBox
              oscillatorData={getBoxControlData('oScillators32KhzController')}
              cx={cx}
            />
            <Gclk0ControllerBox
              gclk0Controller={getBoxControlData('gclkGen0Box')}
              cx={cx}
            />
            <Gclk1ControllerBox
              gclk1Controller={getBoxControlData('gclkGen1Box')}
              cx={cx}
            />
            <GclkXControllerBox
              controller={getBoxControlData('gclkGenXBox')}
              cx={cx}
            />
            <MainClockController
              mainClockController={getBoxControlData('mainClockBox')}
              cx={cx}
            />
            <RTCClockController
              rtcClockController={getBoxControlData('rtcClockSelBox')}
              cx={cx}
            />
            <PeripheralClockControllerBox cx={cx} />

            {/* <CustomLogic cx={cx} /> */}
          </div>
        </div>
      </>
    );
  } catch (error) {
    console.log(error);
    return <>Error Occurred! </>;
  }
};
export default MainBlock;
