import streamlit as st


st.title('Tax Calculator-2025')

st.image('https://github.com/yousuf9292/TaxCalculator/blob/main/tax25.PNG')

annual_taxable_amount=st.number_input(label="Annual Taxable Amount",placeholder='Enter Taxable Amount')
calculation=st.button("Calculation")

def identifying_slab_25():
    if calculation:
        if annual_taxable_amount<=600000:
            st.text("No Tax")
        elif annual_taxable_amount>600000 and annual_taxable_amount<=1200000:
            st.text("Tax % As Per Slab: 5.0%")
            taxperappinc=annual_taxable_amount-600000
            #st.text("Tax %age Applied Income: "+str(taxperappinc))
            tax_as_per_slab=round((taxperappinc*5.0)/100)
            st.text("Tax As Per Slab: " + str(tax_as_per_slab))
            fixed_tax=0
            total_yearly_tax=tax_as_per_slab+fixed_tax
            st.markdown(f'<p style=color:green>Annual Income Tax: {str(total_yearly_tax)}</p>',unsafe_allow_html=True)
            monthly_tax=round(total_yearly_tax/12)
            st.markdown(f"<p style=color:green>Monthly Income Tax: {str(monthly_tax)}</p>",unsafe_allow_html=True)
            tax_paid_this_year=round((total_yearly_tax/annual_taxable_amount)*100,4)
            st.markdown(f"<p style=color:green>Income Tax Ratio: {str(tax_paid_this_year)}%</p>",unsafe_allow_html=True)
        elif annual_taxable_amount>1200000 and annual_taxable_amount<=2200000:
            st.text("Fixed Tax: 30,000")
            st.text("Tax % As Per Slab : 15.0%")
            taxperappinc=annual_taxable_amount-1200000
            #st.text("Tax %age Applied Income: "+str(taxperappinc))
            tax_as_per_slab=round((taxperappinc*15.0)/100)
            st.text("Tax As Per Slab: " + str(tax_as_per_slab))
            fixed_tax=30000
            total_yearly_tax=tax_as_per_slab+fixed_tax
            st.markdown(f'<p style=color:green>Annual Income Tax: {str(total_yearly_tax)}</p>',unsafe_allow_html=True)
            monthly_tax=round(total_yearly_tax/12)
            st.markdown(f"<p style=color:green>Monthly Income Tax: {str(monthly_tax)}</p>",unsafe_allow_html=True)
            tax_paid_this_year=round((total_yearly_tax/annual_taxable_amount)*100,4)
            st.markdown(f"<p style=color:green>Income Tax Ratio: {str(tax_paid_this_year)}%</p>",unsafe_allow_html=True)
        elif annual_taxable_amount>2200000 and annual_taxable_amount<=3200000:
            st.text("Fixed Tax: 180,000")
            st.text("Tax % As Per Slab: 25.0%")
            taxperappinc=annual_taxable_amount-2200000
            #st.text("Tax %age Applied Income: "+str(taxperappinc))
            tax_as_per_slab=round((taxperappinc*25.0)/100)
            st.text("Tax As Per Slab: " + str(tax_as_per_slab))
            fixed_tax=180000
            total_yearly_tax=tax_as_per_slab+fixed_tax
            st.markdown(f'<p style=color:green>Annual Income Tax: {str(total_yearly_tax)}</p>',unsafe_allow_html=True)
            monthly_tax=round(total_yearly_tax/12)
            st.markdown(f"<p style=color:green>Monthly Income Tax: {str(monthly_tax)}</p>",unsafe_allow_html=True)
            tax_paid_this_year=round((total_yearly_tax/annual_taxable_amount)*100,4)
            st.markdown(f"<p style=color:green>Income Tax Ratio: {str(tax_paid_this_year)}%</p>",unsafe_allow_html=True)
        elif annual_taxable_amount>3200000 and annual_taxable_amount<=4100000:
            st.text("Fixed Tax: 430,000")
            st.text("Tax % As Per Slab: 30.0%")
            taxperappinc=annual_taxable_amount-3200000
            #st.text("Tax %age Applied Income: "+str(taxperappinc))
            tax_as_per_slab=round((taxperappinc*30.0)/100)
            st.text("Tax As Per Slab: " + str(tax_as_per_slab))
            fixed_tax=430000
            total_yearly_tax=tax_as_per_slab+fixed_tax
            st.markdown(f'<p style=color:green>Annual Income Tax: {str(total_yearly_tax)}</p>',unsafe_allow_html=True)
            monthly_tax=round(total_yearly_tax/12)
            st.markdown(f"<p style=color:green>Monthly Income Tax: {str(monthly_tax)}</p>",unsafe_allow_html=True)
            tax_paid_this_year=round((total_yearly_tax/annual_taxable_amount)*100,4)
            st.markdown(f"<p style=color:green>Income Tax Ratio: {str(tax_paid_this_year)}%</p>",unsafe_allow_html=True)
        elif annual_taxable_amount>4100000:
            st.text("Fixed Tax: 700,000")
            st.text("Tax % As Per Slab: 35%")
            taxperappinc=annual_taxable_amount-4100000
            #st.text("Tax %age Applied Income: "+str(taxperappinc))
            tax_as_per_slab=round((taxperappinc*35.0)/100)
            st.text("Tax As Per Slab: " + str(tax_as_per_slab))
            fixed_tax=700000
            total_yearly_tax=tax_as_per_slab+fixed_tax
            st.markdown(f'<p style=color:green>Annual Income Tax: {str(total_yearly_tax)}</p>',unsafe_allow_html=True)
            monthly_tax=round(total_yearly_tax/12)
            st.markdown(f"<p style=color:green>Monthly Income Tax: {str(monthly_tax)}</p>",unsafe_allow_html=True)
            tax_paid_this_year=round((total_yearly_tax/annual_taxable_amount)*100,4)
            st.markdown(f"<p style=color:green>Income Tax Ratio: {str(tax_paid_this_year)}%</p>",unsafe_allow_html=True)

identifying_slab_25()
