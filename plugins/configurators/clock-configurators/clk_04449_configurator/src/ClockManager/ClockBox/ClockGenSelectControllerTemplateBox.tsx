import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import { useContext, useEffect, useState } from 'react';
import {
    CheckBoxDefault,
    configSymbolApi,
    InputNumberDefault,
    KeyValueSetRadio,
    PluginConfigContext,
    useBooleanSymbol,
    useIntegerSymbol,
    useKeyValueSetSymbol,
} from '@mplab_harmony/harmony-plugin-client-lib';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import { GetClockDisplayFreqValue } from 'clock-common/lib/Tools/Tools';
import {
    getDynamicLabelsFromJSON,
} from 'clock-common/lib/Tools/ClockJSONTools';
import LoadDynamicFreqencyLabels from 'clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels';
import { GetButton } from '../ClockHelper/LoadDynamicInputNoComponents';
import { Dialog } from 'primereact/dialog';
import ClockGenAutoCalc from './ClockGenAutoCalc';

const ClockGenSelectControllerTemplateBox = (props: {
    index: string;
    componentId: string;
    ClkGenControllerData: ControlInterface[];
    cx: (...classNames: string[]) => string;
}) => {

    const { componentId = 'core' } = useContext(PluginConfigContext);

    const [dialogStatus, setdialogStatus] = useState(false);

    function clkGenAutoCalculationButtonClicked() {
        setdialogStatus(true);
    }

    const dialogClosed = (acceptStatus: boolean) => {
        setdialogStatus(false);
    };


    const isClkGenEnabled = useBooleanSymbol({
        componentId,
        symbolId: 'clkGen' + props.index + 'Enable'
    });

    const isClkGenDivEnabled = useBooleanSymbol({
        componentId,
        symbolId: 'clkGen' + props.index + 'IsDividerEnabled'
    });

    const clockSource = useKeyValueSetSymbol({
        componentId,
        symbolId: 'clkGen' + props.index + 'CON__NOSC'
    });

    const clkGenOutfreq = useIntegerSymbol({
        componentId,
        symbolId: 'clkGen' + props.index + 'OutFrequency'
    });

    const clkSrcFreq = useIntegerSymbol({
        componentId,
        symbolId: 'clkGen' + props.index + 'ClkSrcFrequency'
    });

    let clkGenSymbols = [
        'clkGen' + props.index + 'enableFailSafeClock',
        'clkGen' + props.index + 'CON__BOSC'
    ];

    let clkGenResetSymbols = [
        'clkGen' + props.index + 'CON__NOSC',
        'clkGen' + props.index + 'IsDividerEnabled',
        'clkGen' + props.index + 'DIV__INTDIV',
        'clkGen' + props.index + 'DIV__FRACDIV',
        'clkGen' + props.index + 'enableFailSafeClock',
        'clkGen' + props.index + 'CON__BOSC'
    ];
    type ClkGenPaneType = {
        [key: string]: string;
    };
    type ClkGenFrequencies = {
        [key: string]: number;
    };

    const clkGenFrequencies: ClkGenFrequencies = {
        "CLKGEN1": 200000000,
        "CLKGEN2": 8000000,
        "CLKGEN3": 8000000,
        "CLKGEN4": 100000000,
        "CLKGEN5": 400000000,
        "CLKGEN6": 320000000,
        "CLKGEN7": 500000000,
        "CLKGEN8": 320000000,
        "CLKGEN9": 320000000,
        "CLKGEN10": 400000000,
        "CLKGEN11": 320000000,
        "CLKGEN12": 200000000,
        "CLKGEN13": 200000000
    };
    const index = props.index;
    const key: any = 'CLKGEN' + index

    const maxClkGenOut = clkGenFrequencies[key]
    const maxClkGenDivOutFreq = Math.min(clkSrcFreq.value / 2, maxClkGenOut)
    const clkGenOutfreqVal = Number(clkGenOutfreq.value);
    const textColorClkGenOutFreq = clkGenOutfreqVal > maxClkGenOut ? 'red' : 'black';

    const clkGenPane: ClkGenPaneType =
    {
        "CLKGEN1": "System Clock and Universal Peripheral Bus (UPB)",
        "CLKGEN2": "FRC",
        "CLKGEN3": "BFRC",
        "CLKGEN4": "RAM BIST and NVM BIST",
        "CLKGEN5": "PWM",
        "CLKGEN6": "ADC",
        "CLKGEN7": "PDM DAC",
        "CLKGEN8": "UART",
        "CLKGEN9": "SPI",
        "CLKGEN10": "PTG",
        "CLKGEN11": "BiSS",
        "CLKGEN12": "CCP and REFO1",
        "CLKGEN13": "CLC, IOIM and REFO2"
    }

    const value = clkGenPane[key];
    const clkGenName = "Clock Generator " + index;
    const maxFreqLabel = " (Max Frequency = " + GetClockDisplayFreqValue(maxClkGenOut) + ")";
    const inputClockDescription = "Clock Input for " + value;

    const [dynamicLabelSymbolsInfo] = useState(() => getDynamicLabelsFromJSON(props.ClkGenControllerData));

    const [intdivTooltip, setIntdivTooltip] = useState(props.index);
    const [fracdivTooltip, setFracdivTooltip] = useState(props.index);

    useEffect(() => {
        configSymbolApi.getSymbol(componentId, 'clkGen' + props.index + 'DIV__INTDIV')
            .then((data) => setIntdivTooltip(`Min: ${data.min}, Max: ${data.max}`));
            configSymbolApi.getSymbol(componentId, 'clkGen' + props.index + 'DIV__FRACDIV')
            .then((data) => setFracdivTooltip(`Min: ${data.min}, Max: ${data.max}`));    
    }, [props.index]);


    return (
        <div>
            <label
                className={props.cx('clockGenPaneName')}
            >
                <span style={{ fontWeight: 'bold' }}>{clkGenName} </span>
                <span style={{ fontWeight: 'bold', color: textColorClkGenOutFreq }}>{maxFreqLabel} </span>
            </label>
            <label
                className={props.cx('clockInputLabelDescription')}
            >
                <span style={{ fontWeight: 'bold' }}>{inputClockDescription} </span>
            </label>
            <KeyValueSetRadio
                keyValueSetSymbolHook={clockSource}
                classPrefix={'ClockGenRadio'}
                labelClassPrefix={'ClockGenRadioName'}
                classResolver={props.cx}
                disabled={!isClkGenEnabled.value}
            />
            <LoadDynamicFreqencyLabels
                componentId={componentId}
                dynamicLabelSymbolsInfo={dynamicLabelSymbolsInfo}
                cx={props.cx}
            />
            <CheckBoxDefault
                componentId={componentId}
                symbolId={'clkGen' + props.index + 'Enable'}
                className={props.cx('clkGenEnable')}
            />
            {props.index != '4' &&
                <PlainLabel
                    disPlayText={'Use Clock Divider'}
                    className={props.cx('clockGenDivEn')}
                />}
            {props.index != '4' &&
                <CheckBoxDefault
                    componentId={componentId}
                    symbolId={'clkGen' + props.index + 'IsDividerEnabled'}
                    className={props.cx('clockGenDivCheckBox')}
                    disabled={!isClkGenEnabled.value}
                />}
            {props.index != '4' &&
                <InputNumberDefault
                    componentId={componentId}
                    symbolId={'clkGen' + props.index + 'DIV__INTDIV'}
                    tooltip={intdivTooltip}
                    className={props.cx('clockGenIntdiv')}
                    disabled={!isClkGenEnabled.value}
                />}
            {props.index != '4' &&
                <InputNumberDefault
                    componentId={componentId}
                    symbolId={'clkGen' + props.index + 'DIV__FRACDIV'}
                    className={props.cx('clockGenFracdiv')}
                    disabled={!isClkGenEnabled.value}
                    tooltip={fracdivTooltip}
                //style={{!isClkGenEnabled.value ? opacity:0.5}}
                />}

            <label
                className={props.cx('clockGenOutFreq')}
            >
                <span style={{ fontWeight: 'bold', color: textColorClkGenOutFreq }}>{isClkGenEnabled.value ? GetClockDisplayFreqValue(clkGenOutfreqVal) : '0 Hz'} </span>
                {/* <span style={{ color: 'blue' }}>{'<= ' + GetClockDisplayFreqValue(maxClkGenOut)} </span> */}
            </label>
            {/* {props.index != '4' && isClkGenDivEnabled.value && <PlainLabel
                disPlayText={GetClockDisplayFreqValue(Number(clkSrcFreq.value))}
                className={props.cx('clockGenSrcFreq')}
            />} */}
            <PlainLabel
                disPlayText={'Clock Gen ' + props.index + ' Frequency'}
                className={props.cx('clockGenFreqLabel')}
            //redColorStatus={textColorClkGenOutFreq === 'red' ? true : false}
            />
            <SettingsDialog
                tooltip={'Clock Generator ' + props.index + ' Advanced Settings'}
                componentId={componentId}
                className={props.cx('clkGen_Settings')}
                symbolArray={clkGenSymbols}
                disabled={!isClkGenEnabled.value}
                dialogWidth='50rem'
                dialogHeight='40rem'
            />
            <ResetSymbolsIcon
                tooltip={'Reset Clock Generator ' + props.index + ' Settings to default value'}
                className={props.cx('clkGen_Reset')}
                componentId={componentId}
                resetSymbolsArray={clkGenResetSymbols}
                disabled={!isClkGenEnabled.value}
            />
            {isClkGenDivEnabled.value &&
                <GetButton
                    buttonDisplayText={'Auto Calculate...'}
                    className={props.cx('ClockGenAutoCalcButton')}
                    toolTip={'click here for Clock Generator Auto Calculation'}
                    buttonClick={clkGenAutoCalculationButtonClicked}
                    disabled={!isClkGenEnabled.value}
                />}
            <Dialog
                header={'Auto Calculate Clock Generator ' + props.index + ' Output frequency'}
                visible={dialogStatus}
                maximizable={true}
                style={{ width: '55rem', height: '45rem' }}
                onHide={() => {
                    dialogClosed(false);
                }}>
                <ClockGenAutoCalc
                    index={props.index}
                    componentId={componentId}
                    inputClkSrcFreq={clkSrcFreq.value}
                    reqClkSrcFreq={clkGenOutfreq.value}
                    maxClkGenFreq={maxClkGenDivOutFreq}
                    close={() => {
                        dialogClosed(false);
                    }}
                />
            </Dialog>
        </div>
    )

};

export default ClockGenSelectControllerTemplateBox;