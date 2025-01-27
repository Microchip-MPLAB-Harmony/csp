import { PluginConfigContext, useBooleanSymbol } from '@mplab_harmony/harmony-plugin-client-lib';
import positions from '../Resources/data/positions.module.css';
import styles from './block-diagram-view.module.css';
import tabCss from '../Styles/tab.module.css';
import { ConfirmDialog } from 'primereact/confirmdialog';
import { MenuItem } from 'primereact/menuitem';
import { useContext, useEffect, useState } from 'react';
import ClockJson from '../Resources/data/controls.json';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import { ReactComponent as ClockBlockDiagram } from '../Resources/data/react_clk_04449.svg';
import { initializeSVG, updateSVGForClockGen1Block, updateSVGForCommonClockBlock } from "./SVGHandler";  
import {
  createClassResolver,
  PluginToolbar,
  usePannableContainer,
  useZoomableContainer
} from '@mplab_harmony/harmony-plugin-client-lib';
import PLLControllerBox from './PllControllerBox';
import ClockGenControllerBox from './ClockBox/ClockGenControllerBox';
import ExtClkSrcControllerBox from './ExtClkSrcControllerBox';
import ClockGen2and3ControllerBox from './ClockBox/ClockGen2And3ControllerBox';
import { ListBox } from 'primereact/listbox';
import ClockGenSelectControllerTemplateBox from './ClockBox/ClockGenSelectControllerTemplateBox';

export let controlJsonData = ClockJson as ControlInterface[];
export const cx = createClassResolver(positions, styles, tabCss);

const MainView = () => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const zoomableContainer = useZoomableContainer();
  const pannableContainer = usePannableContainer();

  useEffect(() => { }, []);

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

  const isClkGen1DivEnabled = useBooleanSymbol({
    componentId,
    symbolId: 'clkGen' + '1' + 'IsDividerEnabled'
  });

  interface Tab {
    name: string;
    index: string;
    status: string;
  }

  const generateClkGenTabs = (maxClkGen: number): Tab[] => {
    const refClkTabs: Tab[] = [];
    for (let i = 4; i < maxClkGen; i++) {
      refClkTabs.push({
        name: `CLKGEN ${i}`,
        index: `${i}`,
        status: `clkGen${i}Enable`,
      });
    }
    return refClkTabs;
  };

  const maxClkGen = 14;
  const clkGenTabs = generateClkGenTabs(maxClkGen);

  const [value, setValue] = useState<Tab | null>(clkGenTabs[0]);

  const clkGenIndex = value?.name ? value.index : '4';
  const clkGenSymbolId = 'clkGen' + clkGenIndex + 'IsDividerEnabled';
  const clkGenHook = useBooleanSymbol({
    componentId,
    symbolId: clkGenSymbolId
  });
  useEffect(() => {
    initializeSVG(componentId, cx);
  }, []);
  
  useEffect(() => {
    if (isClkGen1DivEnabled.value) {
      updateSVGForClockGen1Block(false);
    } else {
      updateSVGForClockGen1Block(true);
    }
  }, [isClkGen1DivEnabled.value]);

  useEffect(() => {
    if (clkGenHook.value) {
      updateSVGForCommonClockBlock(false);
    } else {
      updateSVGForCommonClockBlock(true);
    }
  }, [clkGenHook.value]);
  const tabTemplate = (option: any) => {
    // eslint-disable-next-line react-hooks/rules-of-hooks
    const clkGenEnable = useBooleanSymbol({
      componentId,
      symbolId: option.status
    });
    return (
      <div
        style={{ fontSize: '10px' }}
        className={clkGenEnable.value ? cx('enable') : cx('disable')}>
        {option.name}
      </div>
    );
  };

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
          <ClockBlockDiagram id="clk-dspic33-main-image"></ClockBlockDiagram>
          <ListBox
            className={cx('clockGenButton')}
            value={value}
            options={clkGenTabs}
            optionLabel='name'
            itemTemplate={tabTemplate}
            onChange={(e) => setValue(e.value)}
          />
          <ExtClkSrcControllerBox
            ExtClkSrcControllerData={getBoxControlData('ExtClkSrcBox')}
            cx={cx}
          />
          <PLLControllerBox
            index='1'
            PLLControllerData={getBoxControlData('Pll1ControllerBox')}
            cx={cx}
          />
          <PLLControllerBox
            index='2'
            PLLControllerData={getBoxControlData('Pll2ControllerBox')}
            cx={cx}
          />
          <ClockGenControllerBox
            ClkGenControllerData={getBoxControlData('ClkGen1Box')}
            cx={cx}
          />
          <ClockGenSelectControllerTemplateBox
            index={value?.name ? value.index : '4'}
            ClkGenControllerData={getBoxControlData('ClkGenBox')}
            componentId={componentId}
            cx={cx}
          />
          <ClockGen2and3ControllerBox
            ClkGen2and3ControllerData={getBoxControlData('ClkGen2and3Box')}
            cx={cx}
          />
        </div>
      </div >
    </>
  );
};

export default MainView;
