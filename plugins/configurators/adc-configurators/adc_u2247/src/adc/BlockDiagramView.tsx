import adcSVG from '../images/react_adc_u2247.svg';
import { Button } from 'primereact/button';
import positions from './positions.module.css';
import styles from './block-diagram-view.module.css';
import { useState } from 'react';
import { Dialog } from 'primereact/dialog';
import ChannelSequence from './channel-sequence/ChannelSequence';
import {
  usePannableContainer,
  useZoomableContainer,
  CheckBox,
  DropDown,
  PluginToolbar,
  createClassResolver,
  InputNumber,
  ComboRadio
} from '@mplab_harmony/harmony-plugin-client-lib';
import { MenuItem } from 'primereact/menuitem';
import useBlockDiagramViewModel from './BlockDiagramViewModel';
import Summary from './summary/Summary';

const cx = createClassResolver(positions, styles);

function BlockDiagramView() {
  const [channelSequenceDialogVisible, setChannelSequenceDialogVisible] = useState(false);

  const [summaryDialogVisible, setSummaryDialogVisible] = useState(false);

  const pannableContainer = usePannableContainer();
  const zoomableContainer = useZoomableContainer();

  const {
    salveEnable,
    startEventInput,
    conversionTrigger,
    flushEventInput,
    enableUserSequenceMode,
    enableRunInStandby,
    enableOnDemandControl,
    prescaler,
    prescalerValue,
    resultResolution,
    positiveInputCombo,
    negativeInputCombo,
    accumulatedSampelsCombo,
    rightShiftsNumbers,
    sampleLength,
    referenceCombo,
    convTimeValue,
    highThresholdSpinner,
    lowThresholdSpinner,
    comparsionModeCombo,
    enableWinmonInterrupt,
    enableWinmonEvenOut,
    enableleft_alignedResult,
    enableResultInterrupt,
    enableResultIEvent
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
        title='ADC Configurator'
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
            <div
              className={cx('slaveEnable')}
              style={{
                display: 'flex',
                gap: '5px',
                alignItems: 'center',
                justifyContent: 'center'
              }}>
              <CheckBox
                booleanSymbolHook={salveEnable}
                hidden={false}
                disabled={!salveEnable.visible}
                inputId='slaveEnable'
                tooltip={!salveEnable.visible ? 'Disabled' : ''}
              />
              <label htmlFor='slaveEnable'>Enable Slave</label>
            </div>
            <DropDown
              keyValueSetSymbolHook={startEventInput}
              className={cx('startEventInput')}
              hidden={false}
              disabled={!startEventInput.visible}
            />

            <ComboRadio
              comboSymbolHook={conversionTrigger}
              classPrefix={'conversionTrigger'}
              classResolver={cx}
              hidden={false}
              disabled={!conversionTrigger.visible}
            />
            <DropDown
              keyValueSetSymbolHook={flushEventInput}
              className={cx('flushEventInput')}
              hidden={false}
              disabled={!flushEventInput.visible}
            />
            <Button
              label='Channel Sequence'
              className={cx('channelSequenceButton')}
              disabled={
                conversionTrigger.value !== 'HW Event Trigger' || !enableUserSequenceMode.value
              }
              onClick={() => setChannelSequenceDialogVisible(true)}></Button>
            <CheckBox
              booleanSymbolHook={enableUserSequenceMode}
              className={cx('enableUserSequenceMode')}
              disabled={conversionTrigger.value !== 'HW Event Trigger'}
            />

            <CheckBox
              booleanSymbolHook={enableRunInStandby}
              className={cx('enableRunInStandby')}
            />
            <CheckBox
              booleanSymbolHook={enableOnDemandControl}
              className={cx('enableOnDemandControl')}
            />
            <DropDown
              keyValueSetSymbolHook={positiveInputCombo}
              className={cx('positiveInputCombo')}
              hidden={false}
              disabled={!positiveInputCombo.visible}
            />
            <DropDown
              keyValueSetSymbolHook={negativeInputCombo}
              className={cx('negativeInputCombo')}
              hidden={false}
              disabled={!negativeInputCombo.visible}
            />
            <DropDown
              keyValueSetSymbolHook={resultResolution}
              className={cx('resultResolution')}
            />
            <InputNumber
              integerSymbolHook={sampleLength}
              className={cx('sampleLength')}
            />
            <DropDown
              keyValueSetSymbolHook={referenceCombo}
              className={cx('referenceCombo')}
            />
            <label className={cx('convTime')}>{convTimeValue}</label>
            <div className={cx('samplingContainer')}>
              <div className={cx('labeledControlContainer')}>
                <label>Accumulated Sampels</label>{' '}
                <DropDown
                  keyValueSetSymbolHook={accumulatedSampelsCombo}
                  hidden={false}
                  style={{ width: '100px' }}
                />
              </div>

              <div className={cx('labeledControlContainer')}>
                <label>Right Shifts</label>{' '}
                <InputNumber
                  integerSymbolHook={rightShiftsNumbers}
                  hidden={false}
                  style={{ width: '100px' }}
                />
              </div>
            </div>
            <DropDown
              keyValueSetSymbolHook={comparsionModeCombo}
              className={cx('comparsionModeCombo')}
            />
            <InputNumber
              integerSymbolHook={highThresholdSpinner}
              className={cx('highThresholdSpinner')}
              hidden={false}
              disabled={!highThresholdSpinner.visible}
            />
            <InputNumber
              integerSymbolHook={lowThresholdSpinner}
              className={cx('lowThresholdSpinner')}
              hidden={false}
              disabled={!lowThresholdSpinner.visible}
            />

            <CheckBox
              booleanSymbolHook={enableWinmonInterrupt}
              className={cx('enableWinmonInterrupt')}
              hidden={false}
              disabled={!enableWinmonInterrupt.visible}
            />
            <CheckBox
              booleanSymbolHook={enableWinmonEvenOut}
              className={cx('enableWinmonEvenOut')}
              hidden={false}
              disabled={!enableWinmonEvenOut.visible}
            />
            <DropDown
              keyValueSetSymbolHook={prescaler}
              className={cx('prescaler')}
              hidden={false}
              disabled={!prescaler.visible}
            />
            <label className={cx('prescalerLabel')}>{prescalerValue}</label>
            <CheckBox
              booleanSymbolHook={enableleft_alignedResult}
              className={cx('enableleft_alignedResult')}
            />
            <CheckBox
              booleanSymbolHook={enableResultInterrupt}
              className={cx('enableResultInterrupt')}
            />
            <CheckBox
              booleanSymbolHook={enableResultIEvent}
              className={cx('enableResultIEvent')}
            />

            <Dialog
              header='Automatic Sequence Configuration'
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
