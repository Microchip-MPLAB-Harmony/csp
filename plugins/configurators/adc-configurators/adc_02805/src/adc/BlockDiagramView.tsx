import { ReactComponent as ADCBlockDiagram } from '../images/react_adc_02805.svg';
import { Button } from 'primereact/button';
import positions from './positions.module.css';
import styles from './block-diagram-view.module.css';
import { useEffect, useState, useContext } from 'react';
import { Dialog } from 'primereact/dialog';
import adc_02805_short_names from '../resources/adc_02805_short_names.json';
import {
  usePannableContainer,
  useZoomableContainer,
  DropDown,
  KeyValueSetCheckBox,
  KeyValueSetRadio,
  BooleanComboBox,
  shortNamesApi,
  PluginConfigContext,
  InputNumber,
  CheckBox,
  PluginToolbar,
  createClassResolver
} from '@mplab_harmony/harmony-plugin-client-lib';
import InputScanConfiguration from './input-scan-configuration/InputScanConfiguration';
import Summary from './summary/Summary';
import useBlockDiagramViewModel from './BlockDiagramViewModel';
import { MenuItem } from 'primereact/menuitem';
import ReferenceVoltage from './components/ReferenceVoltage';
import { initializeSVG } from './SVGHandler';

const cx = createClassResolver(positions, styles);

function BlockDiagramView() {
  const { componentId = 'adc' } = useContext(PluginConfigContext);

  const {
    clockDivider,
    clockSource,
    clockSourceInputFrequency,
    tad,
    voltageReference,
    outputFormat,
    resultBufferMode,
    enableAutoSampling,
    operationMode,
    autoSampleTime,
    conversionTriggerSource,
    interrupt,
    samplesPerInterrupt,
    stopInIdleMode,
    scanEnable,
    positiveInputA
  } = useBlockDiagramViewModel();

  const [channelScanDialogVisible, setChannelScanDialogVisible] = useState(false);
  const [summaryDialogVisible, setSummaryDialogVisible] = useState(false);

  const pannableContainer = usePannableContainer();
  const zoomableContainer = useZoomableContainer();

  useEffect(() => {
    shortNamesApi.applyShortNames(componentId, 'ADC_MENU', adc_02805_short_names);

    initializeSVG(componentId, cx);
  }, []);

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
            <ADCBlockDiagram id='adc_02805-main-image'></ADCBlockDiagram>
            <KeyValueSetRadio
              keyValueSetSymbolHook={clockSource}
              classPrefix='clockSourceRadio'
              classResolver={cx}></KeyValueSetRadio>
            <label
              className={cx('clockSourceInput1')}
              style={{
                fontWeight:
                  clockSource.options[0] === clockSource.selectedOption ? 'bold' : 'initial'
              }}>
              {clockSource.options[0]}
              <br />
              {parseInt(clockSourceInputFrequency.value).toLocaleString()} Hz
            </label>
            <label
              className={cx('clockSourceInput2')}
              style={{
                fontWeight:
                  clockSource.options[1] === clockSource.selectedOption ? 'bold' : 'initial'
              }}>
              {clockSource.options[1]}
              <br />
              8,000,000 Hz
            </label>
            <InputNumber
              integerSymbolHook={clockDivider}
              className={cx('clockDivider')}></InputNumber>
            <label
              className={cx('tad')}
              style={{ color: 'grey' }}>
              {`TAD = ${tad.value.toLocaleString()} ns`}
            </label>
            <ReferenceVoltage
              keyValueSetSymbolHook={voltageReference}
              classPrefix={'voltageReferenceRadio'}
              classResolver={cx}
            />
            <label
              className={cx('avdd')}
              style={{
                fontWeight: voltageReference.selectedOption.includes('AVDD') ? 'bold' : 'initial'
              }}>
              AVDD
            </label>
            <label
              className={cx('vrefh')}
              style={{
                fontWeight: voltageReference.selectedOption.includes('VREF+') ? 'bold' : 'initial'
              }}>
              VREF+
            </label>
            <label
              className={cx('avss')}
              style={{
                fontWeight: voltageReference.selectedOption.includes('AVSS') ? 'bold' : 'initial'
              }}>
              AVSS
            </label>
            <label
              className={cx('vrefl')}
              style={{
                fontWeight: voltageReference.selectedOption.includes('VREF-') ? 'bold' : 'initial'
              }}>
              VREF-
            </label>
            <div className={cx('outputControlContainer', 'defaultOptionsContainer')}>
              <div>Output Format</div>
              <DropDown keyValueSetSymbolHook={outputFormat}></DropDown>

              <div>Result Buffer Mode</div>
              <DropDown keyValueSetSymbolHook={resultBufferMode}></DropDown>
            </div>
            <div className={cx('samplingContainer')}>
              <div className={cx('labeledControlContainer')}>
                <label>Enable Auto Sampling</label>
                <CheckBox booleanSymbolHook={enableAutoSampling}></CheckBox>
              </div>

              <div className={cx('labeledControlContainer')}>
                <label>Operation Mode</label>{' '}
                <DropDown keyValueSetSymbolHook={operationMode}></DropDown>
              </div>

              {conversionTriggerSource.selectedOption === 'Auto Convert' && (
                <div className={`labeledControlContainer`}>
                  <label>Auto Sample Time (nTAD)</label>{' '}
                  <InputNumber
                    integerSymbolHook={autoSampleTime}
                    size={10}
                  />
                </div>
              )}
            </div>
            <DropDown
              className={cx('conversionTriggerSource')}
              keyValueSetSymbolHook={conversionTriggerSource}></DropDown>
            <div className={cx('interruptOptions', 'defaultOptionsContainer')}>
              <div>
                <label>Interrupt</label>
              </div>
              <CheckBox booleanSymbolHook={interrupt}></CheckBox>

              <div>
                <label>Samples per Interrupt</label>
              </div>
              <DropDown keyValueSetSymbolHook={samplesPerInterrupt}></DropDown>

              <div>
                <label>Stop in Idle Mode</label>
              </div>
              <KeyValueSetCheckBox
                keyValueSetSymbolHook={stopInIdleMode}
                trueOption='Discontinue operation in Idle mode'
                falseOption='Continue operation in Idle mode'></KeyValueSetCheckBox>
            </div>

            <BooleanComboBox
              booleanSymbolHook={scanEnable}
              trueOption='Input Scan'
              falseOption='Do not Scan'
              className={cx('scanEnable')}></BooleanComboBox>

            <DropDown
              className={cx('positiveInputA')}
              keyValueSetSymbolHook={positiveInputA}
              disabled={!positiveInputA.visible}
              hidden={false}></DropDown>
            <Button
              className={cx('channelScanSettings')}
              label='Channel Scan'
              disabled={!scanEnable.value}
              onClick={() => setChannelScanDialogVisible(true)}></Button>
            <Dialog
              header='ADC Input Channel Scan Configuration'
              visible={channelScanDialogVisible}
              maximizable={true}
              onHide={() => setChannelScanDialogVisible(false)}>
              <InputScanConfiguration></InputScanConfiguration>
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
