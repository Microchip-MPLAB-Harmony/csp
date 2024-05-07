import { Accordion, AccordionTab } from "primereact/accordion";
import CommonADCSummary from "./CommonADCSummary";
import DMASequenceSummary from "./DMASequenceSummary";
import { useSummaryData } from "./useSummaryData";
export type SummaryDataProps = {
  accordionHeader: string;
  summaryDetails: FieldsetDetails[] | Symbols[];
};
export type FieldsetDetails = {
  fieldSetHeader: string;
  symbols: Symbols[];
};
export type Symbols = {
  label: string;
  value: string | number | boolean;
};

export const Summary = () => {
  const {summaryData} = useSummaryData()
  const AccordTab = (summary: SummaryDataProps) => {
    if (summary.accordionHeader === "General ADC Config") {
      return (
        <CommonADCSummary
          fieldsetDetails={summary.summaryDetails as FieldsetDetails[]}
        />
      );
    } else if (summary.accordionHeader === "DMA Sequencer") {
      return <DMASequenceSummary />;
    } else if (summary.accordionHeader === "Pin") {
      //return respected UI
      return null;
    } else return null;
  };
  return (
    <div>
      <Accordion activeIndex={0} style={{ width: "80vw" }}>
        {summaryData.map((summary: SummaryDataProps) => {
          return (
            <AccordionTab
              key={summary.accordionHeader}
              header={summary.accordionHeader}
            >
              {AccordTab(summary)}
            </AccordionTab>
          );
        })}
      </Accordion>
    </div>
  );
};
