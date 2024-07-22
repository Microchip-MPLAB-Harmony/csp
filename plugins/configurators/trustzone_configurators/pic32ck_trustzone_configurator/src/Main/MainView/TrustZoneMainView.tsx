import { useEffect, useState } from 'react';
import { TabPanel, TabView } from 'primereact/tabview';
import Peripheral from '../Peripheral/Peripheral';
import { ConfirmDialog } from 'primereact/confirmdialog';
import styles from './block-diagram-view.module.css';
import Memory from '../Memory/Memory';
import {
  createClassResolver,
  PluginToolbar,
  usePannableContainer,
  useZoomableContainer
} from '@mplab_harmony/harmony-plugin-client-lib';
import { MenuItem } from 'primereact/menuitem';
import { Dialog } from 'primereact/dialog';

export let progressStatus = true;

export let toolBarHeight = '60px';
export let secureColor = 'var(--green-500)';
export let nonSecureCallableColor = 'var(--green-300)';
export let nonSecureColor = 'var(--orange-500)';
export let fixedRegionColor = 'var(--gray-300)';
let portNumber = (window as any).javaConnector.getPortNumber();

let headingName = 'Arm\u00AE TrustZone\u00AE for Armv8-M';

const cx = createClassResolver(styles);

const MainBlock = () => {
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
      label: 'Help',
      icon: 'pi pi-search',
      command: () => LoadHelp()
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

  const LoadHelp = () => {
    window.open(
      'http://localhost:' + portNumber + '/csp/docs/index.html',
      '_blank',
      'toolbar=0,location=0,menubar=0'
    );
  };

  return (
    <>
      <ConfirmDialog />
      <PluginToolbar
        menuItems={items}
        title={headingName}
      />
      <div
        className={cx('pannable-container')}
        ref={pannableContainer.ref}
        {...pannableContainer.props}>
        <div
          className={cx('content-container')}
          ref={zoomableContainer.ref}
          {...zoomableContainer.props}>
          <TabView>
            <TabPanel header='Memory Configuration'>
              <Memory />
            </TabPanel>
            <TabPanel header='Peripheral Configuration'>
              <Peripheral />
            </TabPanel>
          </TabView>
        </div>
        <Dialog
          header='TrustZone Summary'
          visible={summaryDialogVisible}
          maximizable={true}
          onHide={() => {
            setSummaryDialogVisible(!summaryDialogVisible);
          }}>
          {/* <Summary /> */}
        </Dialog>
      </div>
    </>
  );
};

export default MainBlock;

export function getIndex(checkValue: any, array: any) {
  return array.findIndex((obj: any) => obj === checkValue);
}
