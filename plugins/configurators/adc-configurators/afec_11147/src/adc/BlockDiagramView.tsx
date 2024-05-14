import adcSVG from '../images/react_afec_11147.svg';
import { Button } from 'primereact/button';
import positions from './positions.module.css';
import styles from './block-diagram-view.module.css';
import { useContext, useState } from 'react';
import { Dialog } from 'primereact/dialog';
import ChannelSequence from './channel-sequence/ChannelSequence';
import ChannelConfigurationView from './channel-configuration/ChannelConfigurationView';
import {
  usePannableContainer,
  useZoomableContainer,
  CheckBox,
  DropDown,
  PluginToolbar,
  createClassResolver,
  KeyValueSetRadio,
  InputNumber,
  PluginConfigContext
} from '@mplab_harmony/harmony-plugin-client-lib';
import { MenuItem } from 'primereact/menuitem';
import useBlockDiagramViewModel from './BlockDiagramViewModel';
import Summary from './summary/Summary';

const cx = createClassResolver(positions, styles);

function getSuffixDigitsAsNumber(value: string) {
  if (value === undefined) {
    return undefined;
  }
  const matches = value.match(/(\d+)$/);
  if (matches) {
    return parseInt(matches[1], 10);
  }
  return undefined;
}

function BlockDiagramView() {
  const { componentId = 'adc' } = useContext(PluginConfigContext);
  const [channelSequenceDialogVisible, setChannelSequenceDialogVisible] = useState(false);
  const [channelConfigurationDialogVisible, setChannelConfigurationDialogVisible] = useState(false);

  const [summaryDialogVisible, setSummaryDialogVisible] = useState(false);

  const pannableContainer = usePannableContainer();
  const zoomableContainer = useZoomableContainer();

  const {
    clockFreq,
    prescalar,
    enableUserSequenceMode,
    triggerSelection,
    conversionMode,
    convTimeValue,
    freqWarning,
    resultResolution,
    resultSign
  } = useBlockDiagramViewModel();

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
      <PluginToolbar
        menuItems={items}
        title={`AFEC ${getSuffixDigitsAsNumber(componentId) ?? ''} Configurator`}
      />
      <div className={cx('block-diagram-container')}>
        <div
          className={cx('pannable-container')}
          ref={pannableContainer.ref}
          {...pannableContainer.props}>
          <div
            className={cx('svg-container')}
            ref={zoomableContainer.ref}
            {...zoomableContainer.props}>
            <img
              src={adcSVG}
              alt='ADC Block Diagram'
              className={cx('main-block-diagram')}
              draggable={false}
            />
            <CheckBox
              booleanSymbolHook={enableUserSequenceMode}
              className={cx('enableUserSequenceMode')}
            />
            <InputNumber
              integerSymbolHook={prescalar}
              className={cx('prescalar')}
            />
            <label className={cx('clockFreq', `${freqWarning.visible ? 'text-red' : null}`)}>
              {clockFreq.value.toLocaleString()} Hz
            </label>
            <label
              className={cx('freqWarning')}
              hidden={!freqWarning.visible}>
              {freqWarning.label}
            </label>

            <label className={cx('prescalarLabel')}>{prescalar.value}</label>

            <DropDown
              className={cx('triggerSelection')}
              keyValueSetSymbolHook={triggerSelection}
              disabled={!triggerSelection.visible}
              hidden={false}
            />
            <KeyValueSetRadio
              keyValueSetSymbolHook={conversionMode}
              classPrefix={'conversionModeRadio'}
              classResolver={cx}></KeyValueSetRadio>
            <DropDown
              keyValueSetSymbolHook={resultResolution}
              className={cx('resultResolution')}
            />
            <DropDown
              keyValueSetSymbolHook={resultSign}
              className={cx('resultSign')}
            />

            <label className={cx('convTime')}>{`${convTimeValue}`}</label>

            <Button
              className={cx('channel-configuration')}
              label='Channel Configuration'
              onClick={() => setChannelConfigurationDialogVisible(true)}></Button>
            <Dialog
              header='Channel Configuration'
              visible={channelConfigurationDialogVisible}
              maximizable={true}
              onHide={() => setChannelConfigurationDialogVisible(false)}>
              <ChannelConfigurationView />
            </Dialog>

            <Button
              className={cx('channel-sequence')}
              label='Channel Sequence'
              disabled={!enableUserSequenceMode.value}
              onClick={() => setChannelSequenceDialogVisible(true)}></Button>
            <Dialog
              header='Channel Sequence Configuration'
              visible={channelSequenceDialogVisible}
              maximizable={true}
              onHide={() => setChannelSequenceDialogVisible(false)}>
              <ChannelSequence />
            </Dialog>
            <Dialog
              header='ADC Configuration Summary'
              visible={summaryDialogVisible}
              maximizable={true}
              onHide={() => setSummaryDialogVisible(false)}>
              <Summary></Summary>
            </Dialog>
          </div>
        </div>
      </div>
    </>
  );
}

export default BlockDiagramView;
