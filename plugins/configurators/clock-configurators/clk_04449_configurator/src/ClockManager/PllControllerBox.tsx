import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import { useContext, useState } from 'react';
import {
    CheckBoxDefault,
    ComboBoxDefault,
    KeyValueSetRadio,
    PluginConfigContext,
    useBooleanSymbol,
    useIntegerSymbol,
    useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import {
    getDynamicLabelsFromJSON,
    getDynamicSymbolsFromJSON
} from 'clock-common/lib/Tools/ClockJSONTools';
import LoadDynamicFreqencyLabels from 'clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels';
import { Dialog } from 'primereact/dialog';
import PLLControllerAutoCalcBox from './PllControllerAutoCalcBox';
import { GetButton, LoadDynamicInputNoComponents } from './ClockHelper/LoadDynamicInputNoComponents';

const PLLControllerBox = (props: {
    index: string
    PLLControllerData: ControlInterface[];
    cx: (...classNames: string[]) => string;
}) => {
    const { componentId = 'core' } = useContext(PluginConfigContext);

    const pllEnable = useBooleanSymbol({
        componentId,
        symbolId: 'pll' + props.index + 'Enable'
    });

    const pllClkSrcFreq = useIntegerSymbol({
        componentId,
        symbolId: 'pll' + props.index + 'ClockSourceFreq'
    });
    const pllCalcPlloFreq = useIntegerSymbol({
        componentId,
        symbolId: 'pll' + props.index + 'calculatedFoutFrequency'
    });
    const pllCalcVcoDivFreq = useIntegerSymbol({
        componentId,
        symbolId: 'pll' + props.index + 'calculatedVCOFrequency'
    });

    const [dialogStatus, setdialogStatus] = useState(false);

    function pllAutoCalculationButtonClicked() {
        setdialogStatus(true);
    }

    const dialogClosed = (acceptStatus: boolean) => {
        setdialogStatus(false);
    };

    const [dynamicSymbolInfo] = useState(() =>
        getDynamicSymbolsFromJSON(props.PLLControllerData)
    );
    const [dynamicLabelSymbolsInfo] = useState(() => getDynamicLabelsFromJSON(props.PLLControllerData));

    const clockSource = useKeyValueSetSymbol({
        componentId,
        symbolId: 'pll' + props.index + 'CON__NOSC'
    });

    let pllSymbols = [
        'pll' + props.index + 'EnableFailSafeClockPll',
        'pll' + props.index + 'CON__BOSC'
    ];

    let pllResetSymbols = [
        'pll' + props.index + 'CON__NOSC',
        'pll' + props.index + 'DIV__PLLPRE',
        'pll' + props.index + 'DIV__PLLFBDIV',
        'pll' + props.index + 'DIV__POSTDIV1',
        'pll' + props.index + 'DIV__POSTDIV2',
        'vco' + props.index + 'DIV__INTDIV',
        'pll' + props.index + 'EnableFailSafeClockPll',
        'pll' + props.index + 'CON__BOSC'
    ];

    return (
        <div>
            <SettingsDialog
                tooltip={'Phase Lock Loop ' + props.index + ' Advanced Settings'}
                componentId={componentId}
                className={props.cx('pll' + props.index + 'Clk_Settings')}
                symbolArray={pllSymbols}
                dialogWidth='50rem'
                dialogHeight='40rem'
                disabled={!pllEnable.value}
            />
            <CheckBoxDefault
                componentId={componentId}
                symbolId={'pll' + props.index + 'Enable'}
                className={props.cx('pll' + props.index + '_enable')}
            />
            <ComboBoxDefault
                componentId={componentId}
                symbolId={'pll' + props.index + 'DIV__POSTDIV1'}
                className={props.cx('pll' + props.index + 'Postdiv1')}
                disabled={!pllEnable.value}
            />
            <ComboBoxDefault
                componentId={componentId}
                symbolId={'pll' + props.index + 'DIV__POSTDIV2'}
                className={props.cx('pll' + props.index + 'Postdiv2')}
                disabled={!pllEnable.value}
            />
            <LoadDynamicInputNoComponents
                componentId={componentId}
                dynamicSymbolsInfo={dynamicSymbolInfo}
                cx={props.cx}
                disable={!pllEnable.value}
            />
            <LoadDynamicFreqencyLabels
                componentId={componentId}
                dynamicLabelSymbolsInfo={dynamicLabelSymbolsInfo}
                cx={props.cx}
            />
            <KeyValueSetRadio
                keyValueSetSymbolHook={clockSource}
                classPrefix={'pll' + props.index + 'ClkRadio'}
                labelClassPrefix={'pll' + props.index + 'ClkRadioName'}
                classResolver={props.cx}
                disabled={!pllEnable.value}
            />
            <ResetSymbolsIcon
                tooltip={'Reset Phase Lock Loop ' + props.index + ' Settings to default value'}
                className={props.cx('pll' + props.index + 'Clk_reset')}
                componentId={componentId}
                resetSymbolsArray={pllResetSymbols}
                disabled={!pllEnable.value}
            />
            <GetButton
                buttonDisplayText={'Auto Calculate...'}
                className={props.cx('pll' + props.index + 'AutoCalc')}
                toolTip={'click here for PLL Auto Calculation'}
                buttonClick={pllAutoCalculationButtonClicked}
                disabled={!pllEnable.value}
            />
            <Dialog
                header='Auto Calculate PLL Dividers'
                visible={dialogStatus}
                maximizable={true}
                style={{ width: '45rem', height: '35rem' }}
                onHide={() => {
                    dialogClosed(false);
                }}>
                <PLLControllerAutoCalcBox
                    index={props.index}
                    componentId={componentId}
                    inputClkSrcFreq={pllClkSrcFreq.value}
                    initialPlloFreq={pllCalcPlloFreq.value}
                    initialPllVcoFreq={pllCalcVcoDivFreq.value}
                    close = {() => {
                        dialogClosed(false);
                    }}
                />
            </Dialog>
        </div>
    );
};

export default PLLControllerBox;