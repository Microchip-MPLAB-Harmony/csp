import { ReactComponent as ClockSAMD21 } from '../Resources/data/react_SAMD21.svg';
import ClockSamC20C21Json from '../Resources/data/controls.json';
import { useContext, useEffect, useState } from 'react';
import { ConfirmDialog } from 'primereact/confirmdialog';
import DFLLController from './ClockBox/DFLLController';
import Oscillators8MHzControllerBox from './ClockBox/Oscillators8MHzControllerBox';
import ClkD21Oscillators32KHzControllerBox from './ClockBox/ClkD21Oscillators32KHzControllerBox';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import useWindowDimensions from 'clock-common/lib/Tools/WindowSize';
import {
  createClassResolver,
  PluginConfigContext,
  PluginToolbar,
  usePannableContainer,
  useZoomableContainer
} from '@mplab_harmony/harmony-plugin-client-lib';

import positions from '../Resources/data/positions.module.css';
import styles from './block-diagram-view.module.css';
import tabCss from '../Styles/tab.module.css';
import { MenuItem } from 'primereact/menuitem';
import Gclk0ControllerBox from './ClockBox/GCLK/Gclk0ControllerBox';
import Gclk1ControllerBox from './ClockBox/GCLK/Gclk1ControllerBox';
import GclkXControllerBox from './ClockBox/GCLK/GclkXControllerBox';
import MainClockController from './ClockBox/MainClockController';
import PeripheralClockControllerBox from './ClockBox/PopUp/PeripheralClockControllerBox';
import FDPLLController from './ClockBox/FDPLL/FDPLLController';
import { initializeSVG } from './SVGhandler';
export let controlJsonData = ClockSamC20C21Json as ControlInterface[];

export const cx = createClassResolver(positions, styles, tabCss);

const MainBlock = () => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

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
  function getBoxControlData(boxId: string) {
    return controlJsonData.filter((e) => e.box_id === boxId);
  }

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
            <ClockSAMD21 id='clk_sam_d21-main-image'></ClockSAMD21>
            <Oscillators8MHzControllerBox
              oscillatorData={getBoxControlData('oscillators_8_MhzControllerBox')}
              cx={cx}
            />
            <FDPLLController
              fdpllControllerData={getBoxControlData('fdpllControllerBox')}
              cx={cx}
            />
            <DFLLController
              dfllControllerData={getBoxControlData('dfllControllerBox')}
              cx={cx}
            />
            <ClkD21Oscillators32KHzControllerBox
              oscillatorData={getBoxControlData('oScillators32KhzController')}
              componentId={componentId}
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
            <PeripheralClockControllerBox cx={cx} />
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
