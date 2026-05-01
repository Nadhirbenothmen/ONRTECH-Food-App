import os
from openai import OpenAI
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

def test_openai_api():
    """Test de la clé API OpenAI"""
    
    # Récupérer la clé API
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("❌ ERREUR: Clé API non trouvée dans les variables d'environnement")
        print("Vérifiez votre fichier .env")
        return False
    
    print(f"🔑 Clé API trouvée: {api_key[:20]}...")
    
    try:
        # Initialiser le client OpenAI
        client = OpenAI(api_key=api_key)
        
        print("🔄 Test de connexion à l'API OpenAI...")
        
        # Test simple avec gpt-4o-mini
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": "Dis simplement 'Test réussi!'"}
            ],
            max_tokens=10
        )
        
        result = response.choices[0].message.content.strip()
        print(f"✅ SUCCÈS: {result}")
        print(f"📊 Modèle utilisé: {response.model}")
        print(f"💰 Tokens utilisés: {response.usage.total_tokens}")
        
        return True
        
    except Exception as e:
        print(f"❌ ERREUR: {e}")
        
        # Analyse des erreurs communes
        error_str = str(e)
        if "401" in error_str:
            print("🔍 Cause probable: Clé API invalide ou permissions insuffisantes")
            print("💡 Solution: Créez une nouvelle clé avec 'All permissions'")
        elif "403" in error_str and "model_not_found" in error_str:
            print("🔍 Cause probable: Modèle non disponible pour votre projet")
            print("💡 Solution: Essayez 'gpt-4o' ou 'gpt-3.5-turbo'")
        elif "429" in error_str:
            print("🔍 Cause probable: Limite de taux atteinte")
        elif "quota" in error_str.lower():
            print("🔍 Cause probable: Quota dépassé")
        
        return False

def test_different_models():
    """Test avec différents modèles"""
    
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        return
    
    client = OpenAI(api_key=api_key)
    
    models_to_test = [
        "gpt-4o",
        "gpt-4o-mini", 
        "gpt-3.5-turbo",
        "gpt-4",
        "gpt-3.5-turbo-16k"
    ]
    
    print("🧪 Test des modèles disponibles...")
    available_models = []
    
    for model in models_to_test:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": "Hi"}],
                max_tokens=5
            )
            print(f"✅ {model}: Disponible")
            available_models.append(model)
        except Exception as e:
            if "model_not_found" in str(e):
                print(f"❌ {model}: Non disponible pour votre projet")
            else:
                print(f"❌ {model}: {str(e)[:60]}...")
    
    if available_models:
        print(f"\n🎯 Modèles recommandés pour votre code: {available_models[0]}")
        return available_models[0]
    else:
        print("\n⚠️ Aucun modèle disponible - vérifiez vos permissions")
        return None

if __name__ == "__main__":
    print("=== TEST DE VOTRE CLÉ API OPENAI ===\n")
    
    # Test principal
    if test_openai_api():
        print("\n=== TEST DES MODÈLES ===")
        recommended_model = test_different_models()
        if recommended_model:
            print(f"\n💡 Utilisez ce modèle dans votre code: model=\"{recommended_model}\"")
    
    print("\n=== FIN DU TEST ===")